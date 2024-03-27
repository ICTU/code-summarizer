"""Main module for the application."""

from langchain.cache import SQLiteCache
from langchain.globals import set_llm_cache

from summarizer.cli import create_argument_parser
from summarizer.summarize import summarize_path


def main() -> None:
    """Run the main program."""
    set_llm_cache(SQLiteCache(database_path=".summarizer_cache.db"))
    args = create_argument_parser().parse_args()
    print(summarize_path(args.path))
