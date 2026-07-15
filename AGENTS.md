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

## Step 11: Model Test Suite

### Test files to create
tests/test_models/test_base_model.py
tests/test_models/test_file_storage.py
tests/test_models/test_user.py
tests/test_models/test_state.py
tests/test_models/test_city.py
tests/test_models/test_place.py
tests/test_models/test_amenity.py
tests/test_models/test_review.py

### Required structure for every test file
#!/usr/bin/python3
"""Tests for the <ClassName> class."""
import unittest
<other imports>


class Test<ClassName>(unittest.TestCase):
    """Test cases for the <ClassName> class."""

    def test_<name>(self):
        """<Complete sentence describing what this test verifies.>"""
        <assertions>


if __name__ == '__main__':
    unittest.main()

### test_base_model.py — required test cases

test_id_is_string:
    assert type(BaseModel().id) is str

test_created_at_is_datetime:
    from datetime import datetime
    assert isinstance(BaseModel().created_at, datetime)

test_updated_at_is_datetime:
    from datetime import datetime
    assert isinstance(BaseModel().updated_at, datetime)

test_save_updates_updated_at:
    m = BaseModel(); old = m.updated_at; m.save()
    assert m.updated_at > old

test_to_dict_has_class_key:
    assert '__class__' in BaseModel().to_dict()

test_to_dict_class_value:
    assert BaseModel().to_dict()['__class__'] == 'BaseModel'

test_to_dict_dates_are_strings:
    d = BaseModel().to_dict()
    assert type(d['created_at']) is str
    assert type(d['updated_at']) is str

test_to_dict_does_not_mutate:
    from datetime import datetime
    m = BaseModel(); m.to_dict()
    assert isinstance(m.created_at, datetime), 'to_dict must not modify original'

test_reconstruction_same_id:
    m = BaseModel()
    assert BaseModel(**m.to_dict()).id == m.id

test_reconstruction_different_object:
    m = BaseModel()
    assert m is not BaseModel(**m.to_dict())

test_str_format:
    assert str(BaseModel()).startswith('[BaseModel]')

### test_file_storage.py — required test cases

test_all_returns_dict:
    from models import storage
    assert type(storage.all()) is dict

test_new_adds_object:
    from models import storage
    from models.base_model import BaseModel
    m = BaseModel(); storage.new(m)
    assert 'BaseModel.' + m.id in storage.all()

test_key_format:
    from models import storage
    from models.base_model import BaseModel
    m = BaseModel(); storage.new(m)
    assert 'BaseModel.' + m.id in storage.all()

test_save_creates_file:
    import os; from models import storage
    storage.save()
    assert os.path.exists('file.json')

test_reload_restores_objects:
    from models import storage
    from models.base_model import BaseModel
    from models.engine.file_storage import FileStorage
    m = BaseModel(); m.save()
    fs = FileStorage(); fs.reload()
    assert 'BaseModel.' + m.id in fs.all()

### test_user.py, test_state.py, test_city.py, test_amenity.py,
### test_place.py, test_review.py — minimum 3 test cases each
Each must include at least:
  test_id_is_string: assert type(<ClassName>().id) is str
  test_created_at_is_datetime: assert isinstance(<ClassName>().created_at, datetime)
  test_str_format: assert str(<ClassName>()).startswith('[<ClassName>]')

### Critical constraints for all model test files
- No test method may call print() directly
- Every test method must have a docstring (complete sentence)
- Test files must pass pycodestyle
- Test files must be executable
