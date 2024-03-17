"""Configuration for the application."""

from pathlib import Path


def skip_file(path: Path) -> bool:
    """Return whether to summarize the file."""
    filenames_to_skip = [".*", "__init__.py", "*.txt", "*.xml", "*.json", "*.png", "*.ico", "*.gif", "*.zip"]
    return any(path.match(filename_to_skip) for filename_to_skip in filenames_to_skip)


def skip_dir(path: Path) -> bool:
    """Return whether to skip the directory."""
    dirs_to_skip = [".*", "*.egg-info", "build", "node_modules", "venv", "__pycache__"]
    for dir_to_skip in dirs_to_skip:
        for part in path.parts:
            if part in (".", ".."):
                continue
            if Path(part).match(dir_to_skip):
                return True
    return False
