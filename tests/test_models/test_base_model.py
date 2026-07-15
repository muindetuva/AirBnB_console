#!/usr/bin/python3
"""Tests for the BaseModel class."""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_id_is_string(self):
        """Verifies that a new BaseModel id is a string."""
        self.assertIs(type(BaseModel().id), str)

    def test_created_at_is_datetime(self):
        """Verifies that created_at is a datetime instance."""
        self.assertIsInstance(BaseModel().created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Verifies that updated_at is a datetime instance."""
        self.assertIsInstance(BaseModel().updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Verifies that save updates the updated_at timestamp."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertGreater(model.updated_at, old_updated_at)

    def test_to_dict_has_class_key(self):
        """Verifies that to_dict includes the __class__ key."""
        self.assertIn("__class__", BaseModel().to_dict())

    def test_to_dict_class_value(self):
        """Verifies that to_dict stores the correct class name."""
        self.assertEqual(BaseModel().to_dict()["__class__"], "BaseModel")

    def test_to_dict_dates_are_strings(self):
        """Verifies that to_dict converts datetime values to strings."""
        data = BaseModel().to_dict()
        self.assertIs(type(data["created_at"]), str)
        self.assertIs(type(data["updated_at"]), str)

    def test_to_dict_does_not_mutate(self):
        """Verifies that to_dict does not mutate datetime attributes."""
        model = BaseModel()
        model.to_dict()
        message = "to_dict must not modify original"
        self.assertIsInstance(model.created_at, datetime, message)

    def test_reconstruction_same_id(self):
        """Verifies that kwargs reconstruction preserves the id."""
        model = BaseModel()
        self.assertEqual(BaseModel(**model.to_dict()).id, model.id)

    def test_reconstruction_different_object(self):
        """Verifies that kwargs reconstruction returns a distinct object."""
        model = BaseModel()
        self.assertIsNot(model, BaseModel(**model.to_dict()))

    def test_str_format(self):
        """Verifies that the string representation starts with class name."""
        self.assertTrue(str(BaseModel()).startswith("[BaseModel]"))


if __name__ == "__main__":
    unittest.main()
