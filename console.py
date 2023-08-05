#!/usr/bin/python3
"""Console's Module"""
import cmd


class HBNBCommand(cmd.Cmd):

    def do_help(self, arg):
        """help command"""
        pass

    def do_EOF(self, line):
        """handle the EOF"""
        return True

    def do_quit(self, arg):
        """quit the cmd"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
