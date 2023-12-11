#!/usr/bin/python3
'''BaseModel subclass.'''
from models.base_model import BaseModel


class City(BaseModel):
    '''city class'''

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """set up city"""
        super().__init__(*args, **kwargs)
