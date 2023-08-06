#!/usr/bin/python3
"""Console's Module"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "


    # def do_help(self, arg):
    #     """help command"""
    #     pass

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
if __name__ == '__main__':
    HBNBCommand().cmdloop()
