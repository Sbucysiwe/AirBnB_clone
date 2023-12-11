#!/usr/bin/python3
'''BaseModel subclass.'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Amenity class.'''

    name = ""

    def __init__(self, *args, **kwargs):
        """Sets up Amenity."""
        super().__init__(*args, **kwargs)
