"""Main module for the application."""

from summarizer.cli import create_argument_parser
from summarizer.summarize import summarize_path


def main() -> None:
    """Run the main program."""
    args = create_argument_parser().parse_args()
    print(summarize_path(args.path))
