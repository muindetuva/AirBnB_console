#!/usr/bin/python3
"""Initialises the models package for the AirBnB console project."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
