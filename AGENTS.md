# AirBnB Console Agent Guide

## Project Context

This project builds the AirBnB clone console in small verified steps.
Follow the step specifications exactly and do not implement future-step
features early.

## Skills

Load .skills/python-alx-style/SKILL.md when creating or editing any .py file.
It handles: shebang line, docstrings, pycodestyle, executable permissions,
empty __init__.py structure, and file endings.
Do not duplicate these rules in step specifications — the skill covers them.

## Step Specifications

## Step 1: BaseModel — New Instance (models/base_model.py)

### Goal
Create the BaseModel class with the new-instance path of __init__ only.
No kwargs reconstruction yet — that is Step 2.
No storage imports anywhere in this file.

### Required imports
import uuid
from datetime import datetime

### __init__(self, *args, **kwargs)
"""Initialises a new BaseModel instance with a unique id and timestamps."""
For now, implement the kwargs-IS-empty branch only:
  self.id = str(uuid.uuid4())
  self.created_at = datetime.now()
  self.updated_at = datetime.now()
Leave the kwargs-is-NOT-empty branch as a stub:
  if kwargs:
      pass  ← will be implemented in Step 2

### __str__(self)
"""Returns the string representation of the instance."""
Return: "[" + type(self).__name__ + "] (" + self.id + ") " + str(self.__dict__)

### save(self)
"""Updates updated_at to the current datetime."""
self.updated_at = datetime.now()
Do NOT call storage.save() yet — added in Step 4.

### to_dict(self)
"""Returns a dictionary of all instance attributes including __class__."""
result = self.__dict__.copy()    ← MUST be .copy() — never self.__dict__ directly
result['__class__'] = type(self).__name__
result['created_at'] = self.created_at.isoformat()
result['updated_at'] = self.updated_at.isoformat()
return result
