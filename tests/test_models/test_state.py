#!/usr/bin/python3
"""Tests for the State class."""

import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_id_is_string(self):
        """Verifies that a new State id is a string."""
        self.assertIs(type(State().id), str)

    def test_created_at_is_datetime(self):
        """Verifies that State created_at is a datetime instance."""
        self.assertIsInstance(State().created_at, datetime)

    def test_str_format(self):
        """Verifies that State string output starts with the class name."""
        self.assertTrue(str(State()).startswith("[State]"))


if __name__ == "__main__":
    unittest.main()
