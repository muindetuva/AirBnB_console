#!/usr/bin/python3
"""Defines the BaseModel class for the AirBnB console project."""

import uuid
from datetime import datetime


class BaseModel:
    """Represents the base model for all console project objects."""

    def __init__(self, *args, **kwargs):
        """Initialises a new BaseModel instance with id and timestamps."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """Returns the string representation of the instance."""
        return (
            "[" + type(self).__name__ + "] (" + self.id + ") "
            + str(self.__dict__)
        )

    def save(self):
        """Updates updated_at to the current datetime."""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary of all attributes including __class__."""
        result = self.__dict__.copy()
        result["__class__"] = type(self).__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
