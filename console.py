#!/usr/bin/python3
"""Console's Module"""
import cmd
from models import storage
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_EOF(self, line):
        """EOF command to EOF the program"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        Usage: create <class_name>
        Example: create Basemodel
        """
        argv = parsing(arg)
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argv[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        Usage: show <class_name> <id>
        Example: show BaseModel 1234-1234-1234
        """
        argl = parsing(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        Usage: destroy <class_name> <id>
        Example: destroy BaseModel 1234-1234-1234
        """
        argl = parsing(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.__objects = objdict
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        Usage: all
        or   : all <class_name>
        """
        argl = parsing(arg)
        objdict = storage.all()
        if len(argl) == 0:
            res = []
            for key in objdict:
                res.append(str(objdict[key]))
            print(res)
        elif argl[0] and argl[0] in HBNBCommand.__classes:
            res = []
            for key in objdict:
                classLen = len(argl[0]) + 2
                if str(objdict[key])[:classLen] == "[{}]".format(argl[0]):
                    res.append(str(objdict[key]))
            print(res)


def parsing(arg):
    brace = re.search(r"\{(.*?)\}", arg)
    bracket = re.search(r"\[(.*?)\]", arg)
    if brace is None:
        if bracket is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lxr = split(arg[:bracket.span()[0]])
            ret = [i.strip(",") for i in lxr]
            ret.append(bracket.group())
            return ret
    else:
        lxr = split(arg[:brace.span()[0]])
        ret = [i.strip(",") for i in lxr]
        ret.append(brace.group())
        return ret


if __name__ == '__main__':
    HBNBCommand().cmdloop()
