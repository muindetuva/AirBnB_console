#!/usr/bin/python3
"""Defines the User class for the AirBnB console project."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user model in the AirBnB console project."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
