#!user/bin/python3
"""Console test cases"""

import unittest
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import uuid


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

    def test_Console_help_create(self):
        """help create"""
        text = ("Creates a new instance of BaseModel, "+
                "saves it (to the JSON file)" +
                "\n        Usage: create <class_name>" +
                "\n        Example: create Basemodel")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("help create") == None)
            self.assertEqual(text, output.getvalue().strip())

    def test_Console_help_destroy(self):
        """help destroy"""
        text = ("Deletes an instance based on the class name" +
                "\n        and id (save the change into the JSON file)" +
                "\n        Usage: destroy <class_name> <id>" +
                "\n        Example: destroy BaseModel 1234-1234-1234")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("help destroy") == None)
            self.assertEqual(text, output.getvalue().strip())

    def test_Console_help_quit(self):
        """help quit"""
        text = ("Quit command to exit the program")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("help quit") == None)
            self.assertEqual(text, output.getvalue().strip())

    def test_Console_help_show(self):
        """help show"""
        text = ("Prints the string representation of " +
                "an instance based on the class name" +
                "\n        Usage: show <class_name> <id>" +
                "\n        Example: show BaseModel 1234-1234-1234")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("help show") == None)
            self.assertEqual(text, output.getvalue().strip())

    def test_Console_help_update(self):
        """help update"""
        text = ("Updates an instance based on the class name" +
                "\n        and id by adding or updating attribute" +
                "\n        Usage: update <class name> <id> <attribute name>" +
                " '<attribute value>'")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("help update") == None)
            self.assertEqual(text, output.getvalue().strip())


class ConsoleCreateTest(unittest.TestCase):
    """Create command"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "_file.json")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("_file.json", "file.json")
        except IOError:
            pass

    def test_Console_create_no_class(self):
        """test create with no class"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **", op.getvalue().strip())

    def test_Console_create_no_existing_class(self):
        """test create with class doesn't exist"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("create Cake")
            self.assertEqual("** class doesn't exist **", op.getvalue().strip())

    def test_Console_create_BaseModel_instance(self):
        """test create BaseModel"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_Console_create_User_instance(self):
        """test create User"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_Console_create_Amenity_instance(self):
        """test create Amenity"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_Console_create_City_instance(self):
        """test create City"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_Console_create_Place_instance(self):
        """test create Place"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_Console_create_Review_instance(self):
        """test create Review"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_Console_create_State_instance(self):
        """test create State"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())


class ConsoleShowTest(unittest.TestCase):
    """test show command"""
    def test_Console_show_no_class(self):
        """test show no class"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **", op.getvalue().strip())

    def test_Console_show_no_existing_class(self):
        """test show class doesn't exist"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("show Cake")
            self.assertEqual("** class doesn't exist **", op.getvalue().strip())

    def test_Console_show_no_id(self):
        """test show class no id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual("** instance id missing **", op.getvalue().strip())

    def test_Console_show_no_existing_id(self):
        """test show class no existing id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("show BaseModel no-id-123")
            self.assertEqual("** no instance found **", op.getvalue().strip())

    def test_Console_show_BaseModel_instance(self):
        """test show BaseModel"""
        obj = BaseModel()
        obj.id = "e2f3b69e-dca0-480f-b20f-ae1a65048a5c"
        obj.created_at = obj.updated_at
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel {}".format(id))
            self.assertEqual("BaseModel." + id, output.getvalue().strip())
