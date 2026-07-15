#!/usr/bin/python3
"""Tests for the HBNBCommand console interpreter."""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand console interpreter."""

    def test_prompt_attribute(self):
        """Test that the console prompt is set correctly."""
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")

    def test_empty_line_no_output(self):
        """Test that an empty line produces no output."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("")
            self.assertEqual(output.getvalue(), "")

    def test_quit_returns_true(self):
        """Test that quit command returns True to exit the loop."""
        self.assertIs(HBNBCommand().onecmd("quit"), True)

    def test_create_missing_class(self):
        """Test create with no class name prints correct error."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual(
                output.getvalue().strip(),
                "** class name missing **"
            )

    def test_create_invalid_class(self):
        """Test create with an invalid class prints correct error."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(
                output.getvalue().strip(),
                "** class doesn't exist **"
            )

    def test_show_missing_class(self):
        """Test show with no class name prints correct error."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show")
            self.assertEqual(
                output.getvalue().strip(),
                "** class name missing **"
            )

    def test_show_invalid_class(self):
        """Test show with an invalid class prints correct error."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(
                output.getvalue().strip(),
                "** class doesn't exist **"
            )

    def test_show_missing_id(self):
        """Test show with no instance id prints correct error."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(
                output.getvalue().strip(),
                "** instance id missing **"
            )

    def test_destroy_missing_class(self):
        """Test destroy with no class name prints correct error."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(
                output.getvalue().strip(),
                "** class name missing **"
            )

    def test_all_invalid_class(self):
        """Test all with an invalid class prints correct error."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(
                output.getvalue().strip(),
                "** class doesn't exist **"
            )

    def test_update_missing_class(self):
        """Test update with no class name prints correct error."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("update")
            self.assertEqual(
                output.getvalue().strip(),
                "** class name missing **"
            )


if __name__ == "__main__":
    unittest.main()
