#!/usr/bin/python3
"""Tests for the City class."""

import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_id_is_string(self):
        """Verifies that a new City id is a string."""
        self.assertIs(type(City().id), str)

    def test_created_at_is_datetime(self):
        """Verifies that City created_at is a datetime instance."""
        self.assertIsInstance(City().created_at, datetime)

    def test_str_format(self):
        """Verifies that City string output starts with the class name."""
        self.assertTrue(str(City()).startswith("[City]"))


if __name__ == "__main__":
    unittest.main()
