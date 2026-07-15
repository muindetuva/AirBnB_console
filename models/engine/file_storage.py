#!/usr/bin/python3
"""Defines JSON file storage for the AirBnB console project."""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Serialises and deserialises model instances to a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds an object to storage using the class-name dot id key."""
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialises stored objects to the JSON storage file."""
        objects = {}
        for key, value in FileStorage.__objects.items():
            objects[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(objects, file)

    def reload(self):
        """Deserialises stored objects from the JSON storage file."""
        classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User,
        }
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                objects = json.load(file)
            for key, value in objects.items():
                class_name = value["__class__"]
                FileStorage.__objects[key] = classes[class_name](**value)
        except FileNotFoundError:
            pass
