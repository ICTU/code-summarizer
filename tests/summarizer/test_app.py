"""Unit tests for the app module."""

import unittest
from unittest.mock import Mock, patch

from langchain_core.messages.base import BaseMessage
from summarizer.app import main


@patch(
    "summarizer.summarize.ChatOpenAI",
    Mock(return_value=Mock(invoke=Mock(return_value=BaseMessage(content="Summary", type="")))),
)
class MainTests(unittest.TestCase):
    """Unit tests for the main function."""

    @patch("pathlib.Path.iterdir", Mock(return_value=[]))
    @patch("pathlib.Path.is_dir", Mock(return_value=True))
    @patch("sys.argv", ["summarize", "valid_path"])
    @patch("sys.stdout.write")
    def test_main(self, mock_write: Mock) -> None:
        """Test the main function."""
        main()
        self.assertEqual("None", mock_write.call_args_list[0][0][0])
