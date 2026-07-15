#!/usr/bin/python3
"""Tests for the Place class."""

import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_id_is_string(self):
        """Verifies that a new Place id is a string."""
        self.assertIs(type(Place().id), str)

    def test_created_at_is_datetime(self):
        """Verifies that Place created_at is a datetime instance."""
        self.assertIsInstance(Place().created_at, datetime)

    def test_str_format(self):
        """Verifies that Place string output starts with the class name."""
        self.assertTrue(str(Place()).startswith("[Place]"))


if __name__ == "__main__":
    unittest.main()
