#!/usr/bin/python3
"""Initialises model test discovery for the AirBnB console project."""

import unittest


def load_tests(loader, tests, pattern):
    """Discovers all model test modules in this package."""
    return loader.discover(
        start_dir=__path__[0],
        pattern="test_*.py",
    )
