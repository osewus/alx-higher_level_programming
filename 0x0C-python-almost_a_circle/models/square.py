#!/usr/bin/python3
"""
Square class definition
"""

from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        instanciation of a square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        get size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        set size
        """
        self.__height = value
        self.__width = value

    def __str__(self):
        """
        returns object as a string
        """
        return ("[Square] ({}) {:d}/{:d} - {:d}".format
                (self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """update"""
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):
        """
            returns the dictionary
            representation of a square
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
