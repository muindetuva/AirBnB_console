#!/usr/bin/python3
"""Tests for the FileStorage class."""

import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_all_returns_dict(self):
        """Verifies that all returns the storage dictionary."""
        self.assertIs(type(storage.all()), dict)

    def test_new_adds_object(self):
        """Verifies that new adds an object to storage."""
        model = BaseModel()
        storage.new(model)
        self.assertIn("BaseModel." + model.id, storage.all())

    def test_key_format(self):
        """Verifies that storage keys use ClassName dot id format."""
        model = BaseModel()
        storage.new(model)
        self.assertIn("BaseModel." + model.id, storage.all())

    def test_save_creates_file(self):
        """Verifies that save creates the JSON storage file."""
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_restores_objects(self):
        """Verifies that reload restores model instances from JSON."""
        model = BaseModel()
        model.save()
        file_storage = FileStorage()
        file_storage.reload()
        self.assertIn("BaseModel." + model.id, file_storage.all())


if __name__ == "__main__":
    unittest.main()
