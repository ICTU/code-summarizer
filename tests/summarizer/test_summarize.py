"""Unit tests for the summarize module."""

import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from langchain_core.messages.base import BaseMessage
from summarizer.summarize import summarize_path
from summarizer.summary import Summary


@patch(
    "summarizer.summarize.ChatOpenAI",
    Mock(return_value=Mock(invoke=Mock(return_value=BaseMessage(content="Summary", type="")))),
)
@patch("summarizer.summarize.Path.read_text", Mock(return_value="File contents"))
class SummarizePathTests(unittest.TestCase):
    """Unit tests for the summerize_path method."""

    def setUp(self) -> None:
        """Set up the test fixtures."""
        self.path = Path()

    @patch("summarizer.summarize.Path.iterdir", Mock(return_value=[]))
    def test_empty_path(self):
        """Test the summary of an empty path."""
        self.assertIsNone(summarize_path(self.path))

    @patch("summarizer.summarize.Path.iterdir", Mock(return_value=[Path("file.py")]))
    @patch("summarizer.summarize.Path.is_file", Mock(return_value=True))
    def test_path_with_one_file(self):
        """Test the summary of a path with one file."""
        self.assertEqual(Summary(Path("file.py"), "Summary"), summarize_path(self.path))

    @patch("summarizer.summarize.Path.iterdir", Mock(side_effect=[[], [Path("file1.py"), Path("file2.py")]]))
    @patch("summarizer.summarize.Path.is_file", Mock(return_value=True))
    def test_path_with_two_files(self):
        """Test the summary of a path with two files."""
        file1_summary = Summary(Path("file1.py"), "Summary")
        file2_summary = Summary(Path("file2.py"), "Summary")
        files_summary = Summary(self.path, "Summary of .", (file1_summary, file2_summary))
        self.assertEqual(files_summary, summarize_path(self.path))

    @patch("summarizer.summarize.Path.iterdir", Mock(side_effect=[[Path("dir")], [], [], []]))
    @patch("summarizer.summarize.Path.is_dir", Mock(return_value=True))
    def test_path_with_one_empty_path(self):
        """Test the summary of a path with one empty path."""
        self.assertIsNone(summarize_path(self.path))

    @patch("summarizer.summarize.Path.iterdir", Mock(side_effect=[[Path("dir")], [], [], [Path("file.py")]]))
    @patch("summarizer.summarize.Path.is_dir", Mock(return_value=True))
    @patch("summarizer.summarize.Path.is_file", Mock(return_value=True))
    def test_path_with_one_path_with_one_file(self):
        """Test the summary of a path with one file."""
        self.assertEqual(Summary(Path("file.py"), "Summary"), summarize_path(self.path))
