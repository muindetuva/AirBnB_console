#!/usr/bin/python3
"""Defines the Review class for the AirBnB console project."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review model in the AirBnB console project."""

    place_id = ""
    user_id = ""
    text = ""
