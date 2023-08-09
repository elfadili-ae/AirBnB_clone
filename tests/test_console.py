#!user/bin/python3
"""Console test cases"""

import unittest
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class ConsolePromptTest(unittest.TestCase):
    """Console class test cases"""
    def test_Console_prompt(self):
        """check the prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_Console_prompt_empty_line(self):
        """check empty line"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue())

    def test_Console_prompt_new_line(self):
        """check new line"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("\n"))
            self.assertEqual("", output.getvalue())

    def test_Console_quit(self):
        """check quit exists"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_Console_eof(self):
        """check eof exists"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class ConsoleHelpTest(unittest.TestCase):
    """help testing"""
    def test_Console_help(self):
        """check help exists"""
        _help = ("Documented commands (type help <topic>):\n" +
                 "========================================\n" +
                 "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("help") == None)
            self.assertEqual(_help, output.getvalue().strip())

    def test_Console_help_EOF(self):
        """help eof"""
        text = "EOF command to EOF the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("help EOF") == None)
            self.assertEqual(text, output.getvalue().strip())

    def test_Console_help_all(self):
        """help all"""
        text = ("Prints all string representation of all" +
                "\n        instances based or not on the class name" +
                "\n        Usage: all" +
                "\n        or   : all <class_name>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("help all") == None)
            self.assertEqual(text, output.getvalue().strip())

    def test_Console_help_count(self):
        """help all"""
        text = ("Return the number of count." +
                "\n        Usage: <class name>.count()." +
                "\n        Example: User.count().")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("help count") == None)
            self.assertEqual(text, output.getvalue().strip())

