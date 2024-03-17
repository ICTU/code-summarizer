"""Command-line interface for the application."""

from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path


def dir_path(path_argument: str) -> Path:
    """Check that the path argument is a valid path."""
    path = Path(path_argument)
    if path.is_dir():
        return path
    message = f"{path_argument} is not a valid path"
    raise ArgumentTypeError(message)


def create_argument_parser() -> ArgumentParser:
    """Create the argument parser."""
    argument_parser = ArgumentParser(description="Summarizes code bases.")
    argument_parser.add_argument("-V", "--version", action="version", version="0.1")
    argument_parser.add_argument("path", type=dir_path, help="path to summarize recursively")
    return argument_parser
