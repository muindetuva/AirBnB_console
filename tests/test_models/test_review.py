#!/usr/bin/python3
"""Tests for the Review class."""

import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_id_is_string(self):
        """Verifies that a new Review id is a string."""
        self.assertIs(type(Review().id), str)

    def test_created_at_is_datetime(self):
        """Verifies that Review created_at is a datetime instance."""
        self.assertIsInstance(Review().created_at, datetime)

    def test_str_format(self):
        """Verifies that Review string output starts with the class name."""
        self.assertTrue(str(Review()).startswith("[Review]"))


if __name__ == "__main__":
    unittest.main()
