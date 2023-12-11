#!/usr/bin/python3
'''BaseModel subclass.'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''review class'''

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """set up Review"""
        super().__init__(*args, **kwargs)
