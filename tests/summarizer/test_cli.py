"""Unit tests for the command-line interface."""

import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from summarizer.cli import create_argument_parser


class ArgumentParserTests(unittest.TestCase):
    """Unit tests for the argument parser."""

    def setUp(self):
        """Override to set up test fixtures."""
        self.argument_parser = create_argument_parser()

    @patch("summarizer.cli.Path.is_dir", Mock(return_value=False))
    @patch("sys.argv", ["summarize", "invalid_path"])
    @patch("sys.stderr.write")
    def test_invalid_path(self, mock_write: Mock) -> None:
        """Test that an invalid path shows an error message."""
        self.assertRaises(SystemExit, self.argument_parser.parse_args)
        self.assertIn("invalid_path is not a valid path", mock_write.call_args_list[1][0][0])

    @patch("summarizer.cli.Path.is_dir", Mock(return_value=True))
    @patch("sys.argv", ["summarize", "valid_path"])
    def test_valid_path(self):
        """Test that a valid path is returned."""
        self.assertEqual(Path("valid_path"), self.argument_parser.parse_args().path)
