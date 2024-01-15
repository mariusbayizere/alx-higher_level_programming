#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """
    Define Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a Base class.

        Args:
            id (int): the identity of Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """function that save of a list of objects to a file.

        Args:
            list_objs (list): A list of reuse Base instance.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                tuple_list1 = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(tuple_list1))

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def from_json_string(json_string):
        """function the serialize of java script string.

        Args:
            json_string (str): a json string represent of a list.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """function that will return list of class from a
        file of in java object notation.
        Returns:
            If the file does not exist - an empty list.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as file:
                tuple_list1 = Base.from_json_string(file.read())
                return [cls.create(**d) for d in tuple_list1]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        function Draw rectangles and squares on a canvas.

        Parameters:
            list_rectangles (list): A list of Rectangle objects to be drawn.
            list_squares (list): A list of Square objects to be drawn.

        Returns:
            None
            """
        pani = turtle.Turtle()
        pani.screen.bgcolor("#b7312c")
        pani.pensize(3)
        pani.shape("turtle")

        pani.color("#ffffff")
        for wiski in list_rectangles:
            pani.showturtle()
            pani.up()
            pani.goto(wiski.x, wiski.y)
            pani.down()
            for i in range(2):
                pani.forward(wiski.width)
                pani.left(90)
                pani.forward(wiski.height)
                pani.left(90)
            pani.hideturtle()

        pani.color("#b5e3d8")
        for lend in list_squares:
            pani.showturtle()
            pani.up()
            pani.goto(lend.x, lend.y)
            pani.down()
            for i in range(2):
                pani.forward(lend.width)
                pani.left(90)
                pani.forward(lend.height)
                pani.left(90)
            pani.hideturtle()

        turtle.exitonclick()

    @staticmethod
    def to_json_string(list_dictionaries):
        """function that make of a list of dictionary.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
