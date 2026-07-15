#!/usr/bin/python3
"""Tests for the User class."""

import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_id_is_string(self):
        """Verifies that a new User id is a string."""
        self.assertIs(type(User().id), str)

    def test_created_at_is_datetime(self):
        """Verifies that User created_at is a datetime instance."""
        self.assertIsInstance(User().created_at, datetime)

    def test_str_format(self):
        """Verifies that User string output starts with the class name."""
        self.assertTrue(str(User()).startswith("[User]"))


if __name__ == "__main__":
    unittest.main()
