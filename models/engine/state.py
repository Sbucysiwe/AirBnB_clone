#!/usr/bin/python3
'''BaseModel subclass.'''
from models.base_model import BaseModel


class State(BaseModel):
    '''state class'''

    name = ""

    def __init__(self, *args, **kwargs):
        """set up State"""
        super().__init__(*args, **kwargs)
