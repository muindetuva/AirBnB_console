#!/usr/bin/python3
"""Provides the command interpreter for the AirBnB console project."""

import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


CLASSES = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}


class HBNBCommand(cmd.Cmd):
    """Implements the interactive AirBnB console command interpreter."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Does nothing when the user enters an empty line."""
        pass

    def do_quit(self, arg):
        """Exits the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exits the command interpreter at end of input."""
        return True

    def do_create(self, arg):
        """Creates a new instance of a supported model class."""
        args = arg.split()
        if not self._validate_class(args):
            return
        instance = CLASSES[args[0]]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of a stored instance."""
        args = arg.split()
        if not self._validate_class(args):
            return
        if not self._validate_id(args):
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """Deletes a stored instance by class name and id."""
        args = arg.split()
        if not self._validate_class(args):
            return
        if not self._validate_id(args):
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Prints string representations for stored model instances."""
        args = arg.split()
        if args and args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        values = []
        for key, value in objects.items():
            if not args or key.startswith(args[0] + "."):
                values.append(str(value))
        print(values)

    def do_update(self, arg):
        """Updates an attribute on a stored instance."""
        args = arg.split()
        if not self._validate_class(args):
            return
        if not self._validate_id(args):
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objects[key], args[2], args[3].strip('"'))
        objects[key].save()

    def _validate_class(self, args):
        """Checks that a class name is present and supported."""
        if not args:
            print("** class name missing **")
            return False
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return False
        return True

    def _validate_id(self, args):
        """Checks that an instance id is present in command arguments."""
        if len(args) < 2:
            print("** instance id missing **")
            return False
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
