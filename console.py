#!/usr/bin/python3
"""Provides the command interpreter for the AirBnB console project."""

import ast
import cmd
import shlex
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
        args = shlex.split(arg)
        if not self._validate_class(args):
            return
        instance = CLASSES[args[0]]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of a stored instance."""
        args = shlex.split(arg)
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
        args = shlex.split(arg)
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
        args = shlex.split(arg)
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
        args = shlex.split(arg)
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
        self._set_instance_attribute(args[0], args[1], args[2], args[3])

    def default(self, line):
        """Handles class-dot command syntax for supported model classes."""
        if "." not in line:
            return super().default(line)
        class_name, remainder = line.split(".", 1)
        command, raw_args = self._parse_dot_command(remainder)
        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return
        if command == "all":
            return self.do_all(class_name)
        if command == "count":
            return self._count_instances(class_name)
        args = self._parse_dot_args(raw_args)
        if command == "show":
            return self.do_show(self._join_args([class_name] + args))
        if command == "destroy":
            return self.do_destroy(self._join_args([class_name] + args))
        if command == "update":
            return self._update_from_dot_command(class_name, args)
        return super().default(line)

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

    def _count_instances(self, class_name):
        """Prints the number of stored instances for a model class."""
        count = 0
        for key in storage.all():
            if key.startswith(class_name + "."):
                count += 1
        print(count)

    def _parse_dot_command(self, remainder):
        """Returns the command name and raw argument text from dot syntax."""
        if "(" not in remainder or not remainder.endswith(")"):
            return remainder, ""
        command, raw_args = remainder.split("(", 1)
        return command, raw_args[:-1]

    def _parse_dot_args(self, raw_args):
        """Parses arguments from class-dot command syntax."""
        if not raw_args.strip():
            return []
        try:
            value = ast.literal_eval("(" + raw_args + ",)")
        except (SyntaxError, ValueError):
            return []
        return list(value)

    def _join_args(self, args):
        """Joins command arguments while preserving quoted string values."""
        return " ".join(shlex.quote(str(arg)) for arg in args)

    def _update_from_dot_command(self, class_name, args):
        """Updates an instance from class-dot update command arguments."""
        if len(args) < 1:
            return self.do_update(class_name)
        if len(args) < 2:
            return self.do_update(self._join_args([class_name, args[0]]))
        if isinstance(args[1], dict):
            for attr_name, attr_value in args[1].items():
                self._set_instance_attribute(
                    class_name, args[0], attr_name, attr_value
                )
            return
        if len(args) < 3:
            command_args = self._join_args([class_name, args[0], args[1]])
            return self.do_update(command_args)
        self._set_instance_attribute(class_name, args[0], args[1], args[2])

    def _set_instance_attribute(
        self, class_name, obj_id, attr_name, attr_value
    ):
        """Sets an attribute on a stored instance and saves storage."""
        key = class_name + "." + obj_id
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        setattr(objects[key], attr_name, attr_value)
        objects[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
