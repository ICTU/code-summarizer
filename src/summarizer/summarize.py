"""Methods to summarize paths and files."""

from pathlib import Path

from langchain_openai import ChatOpenAI

from summarizer.config import skip_dir, skip_file
from summarizer.summary import Summary


class Summarizer:
    """Class to summarize paths and files."""

    def __init__(self) -> None:
        self.llm = ChatOpenAI()

    def summarize_path(self, path: Path) -> Summary | None:
        """Summarize all code in the path, recursively."""
        summaries = [self.summarize_path(subpath) for subpath in self.subpaths(path)]
        summaries.append(self.summarize_files(path))
        return self.summarize_summaries(path, *[summary for summary in summaries if summary is not None])

    def summarize_files(self, path: Path) -> Summary | None:
        """Return a summary for the files on the path."""
        summaries = [self.summarize_file(file_path) for file_path in self.files(path)]
        return self.summarize_summaries(path, *summaries)

    def summarize_file(self, path: Path) -> Summary:
        """Return a summary of the file."""
        contents = path.read_text()
        summary = self.llm.invoke(f"Summarize this file: ```{contents}```")
        return Summary(path, str(summary.content))

    def summarize_summaries(self, path: Path, *summaries: Summary) -> Summary | None:
        """Return a summary of the summaries."""
        if summaries:
            return Summary(path, f"Summary of {path}", summaries=summaries) if len(summaries) > 1 else summaries[0]
        return None

    @staticmethod
    def subpaths(path: Path) -> list[Path]:
        """Return the subpaths of path."""
        return [subpath for subpath in path.iterdir() if subpath.is_dir() and not skip_dir(subpath)]

    @staticmethod
    def files(path: Path) -> list[Path]:
        """Return the files in path."""
        return [subpath for subpath in path.iterdir() if subpath.is_file() and not skip_file(subpath)]


def summarize_path(path: Path) -> Summary | None:
    """Summarize all code in the path, recursively."""
    return Summarizer().summarize_path(path)
