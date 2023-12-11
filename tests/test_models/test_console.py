#!/usr/bin/python3
"""Console testing."""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """Console testing class."""

    def create(self):
        """Instantiate the object."""
        return HBNBCommand()

    def test_quit(self):
        """ Quit method testing.
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """method EQF testing
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
