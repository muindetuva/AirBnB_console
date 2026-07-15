#!/usr/bin/python3
"""Tests for the HBNBCommand console interpreter."""

import os
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage


MODEL_CLASSES = [
    "Amenity",
    "BaseModel",
    "City",
    "Place",
    "Review",
    "State",
    "User",
]


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand console interpreter."""

    def setUp(self):
        """Clear storage before each console test runs."""
        storage.all().clear()

    def tearDown(self):
        """Clear storage and remove the JSON file after each test."""
        storage.all().clear()
        if os.path.exists("file.json"):
            os.remove("file.json")

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

    def test_EOF_returns_true(self):
        """Test that EOF command returns True to exit the loop."""
        self.assertIs(HBNBCommand().onecmd("EOF"), True)

    def test_help_outputs_available_commands(self):
        """Test that help command prints documented console commands."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands", output.getvalue())

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

    def test_create_base_model_adds_instance(self):
        """Test create BaseModel prints an id and stores the instance."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = output.getvalue().strip()
            self.assertTrue(obj_id)
            self.assertIn("BaseModel." + obj_id, storage.all())

    def test_show_base_model_prints_instance(self):
        """Test show BaseModel prints the matching stored instance."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel " + obj_id)
            self.assertIn("[BaseModel] (" + obj_id + ")", output.getvalue())

    def test_destroy_base_model_removes_instance(self):
        """Test destroy BaseModel removes the matching stored instance."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = output.getvalue().strip()
        HBNBCommand().onecmd("destroy BaseModel " + obj_id)
        self.assertNotIn("BaseModel." + obj_id, storage.all())

    def test_all_base_model_prints_instances(self):
        """Test all BaseModel prints stored BaseModel instances."""
        with patch("sys.stdout", new=StringIO()):
            HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn("[BaseModel]", output.getvalue())

    def test_update_base_model_sets_attribute(self):
        """Test update BaseModel sets an attribute on the instance."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = output.getvalue().strip()
        HBNBCommand().onecmd('update BaseModel ' + obj_id + ' name "ALX"')
        self.assertEqual(storage.all()["BaseModel." + obj_id].name, "ALX")

    def test_class_all_dot_syntax_for_all_models(self):
        """Test Class.all() prints stored instances for every model."""
        for class_name in MODEL_CLASSES:
            storage.all().clear()
            with patch("sys.stdout", new=StringIO()):
                HBNBCommand().onecmd("create " + class_name)
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(class_name + ".all()")
                self.assertIn("[" + class_name + "]", output.getvalue())

    def test_class_count_dot_syntax_for_all_models(self):
        """Test Class.count() prints stored instance counts for every model."""
        for class_name in MODEL_CLASSES:
            storage.all().clear()
            with patch("sys.stdout", new=StringIO()):
                HBNBCommand().onecmd("create " + class_name)
                HBNBCommand().onecmd("create " + class_name)
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(class_name + ".count()")
                self.assertEqual(output.getvalue().strip(), "2")

    def test_class_show_dot_syntax_for_all_models(self):
        """Test Class.show(id) prints stored instances for every model."""
        for class_name in MODEL_CLASSES:
            storage.all().clear()
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create " + class_name)
                obj_id = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(class_name + '.show("' + obj_id + '")')
                self.assertIn("[" + class_name + "]", output.getvalue())

    def test_class_destroy_dot_syntax_for_all_models(self):
        """Test Class.destroy(id) removes stored instances for every model."""
        for class_name in MODEL_CLASSES:
            storage.all().clear()
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create " + class_name)
                obj_id = output.getvalue().strip()
            HBNBCommand().onecmd(class_name + '.destroy("' + obj_id + '")')
            self.assertNotIn(class_name + "." + obj_id, storage.all())

    def test_class_update_dot_syntax_for_all_models(self):
        """Test Class.update(id, attr, value) updates every model."""
        for class_name in MODEL_CLASSES:
            storage.all().clear()
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create " + class_name)
                obj_id = output.getvalue().strip()
            command = class_name + '.update("' + obj_id + '", "name", "ALX")'
            HBNBCommand().onecmd(command)
            instance = storage.all()[class_name + "." + obj_id]
            self.assertEqual(instance.name, "ALX")

    def test_class_update_dict_dot_syntax_for_all_models(self):
        """Test Class.update(id, dict) updates every model."""
        for class_name in MODEL_CLASSES:
            storage.all().clear()
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create " + class_name)
                obj_id = output.getvalue().strip()
            command = class_name + '.update("' + obj_id
            command += '", {"name": "ALX", "number": 89})'
            HBNBCommand().onecmd(command)
            instance = storage.all()[class_name + "." + obj_id]
            self.assertEqual(instance.name, "ALX")
            self.assertEqual(instance.number, 89)


if __name__ == "__main__":
    unittest.main()
