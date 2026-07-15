#!/usr/bin/python3
"""Tests for the Amenity class."""

import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_id_is_string(self):
        """Verifies that a new Amenity id is a string."""
        self.assertIs(type(Amenity().id), str)

    def test_created_at_is_datetime(self):
        """Verifies that Amenity created_at is a datetime instance."""
        self.assertIsInstance(Amenity().created_at, datetime)

    def test_str_format(self):
        """Verifies that Amenity string output starts with the class name."""
        self.assertTrue(str(Amenity()).startswith("[Amenity]"))


if __name__ == "__main__":
    unittest.main()
