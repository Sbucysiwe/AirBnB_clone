#!/usr/bin/python3
"""Test for console"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """class test console"""

    def create(self):
        """create intance"""
        return HBNBCommand()

    def test_quit(self):
        """ test for method quit
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """test for method EQF
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
