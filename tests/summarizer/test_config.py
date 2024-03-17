"""Unit tests for the config module."""

import unittest
from pathlib import Path

from summarizer.config import skip_dir, skip_file


class SkipDirTests(unittest.TestCase):
    """Unit tests for the skip_dir method."""

    def test_dirs_to_skip(self):
        """Test that dirs are skipped."""
        for dir_to_skip in ("node_modules", "__pycache__"):
            self.assertTrue(skip_dir(Path(dir_to_skip)))

    def test_dir_to_include(self):
        """Test that dirs are included."""
        for dir_to_include in ("src", "tests", "docs", "./dir", "../other_dir"):
            self.assertFalse(skip_dir(Path(dir_to_include)))


class SkipFileTests(unittest.TestCase):
    """Unit tests for the skip_file method."""

    def test_file_to_skip(self):
        """Test that files are skipped."""
        for filename_to_skip in ("archive.zip", "picture.png", "./this.json"):
            self.assertTrue(skip_file(Path(filename_to_skip)))

    def test_file_to_include(self):
        """Test that files are included."""
        for filename_to_include in ("source.py", "source.java", "docs.md"):
            self.assertFalse(skip_file(Path(filename_to_include)))
