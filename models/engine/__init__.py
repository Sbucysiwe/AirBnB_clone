#!/usr/bin/python3
"""Instantiate a unique FileStorage instance for your application."""
from models.engine.file_storage import FileStorage

"""A FileStorage instance for variable storage."""
storage = FileStorage()
storage.reload()
