#!/usr/bin/python3
""" A class for a square """


class Square:
    """ A class of Square """

    def __init__(self, size=0):
        """ Initialization of class
        Name:
            size: private instance
        Error:
            typeError: if not int
            valueError: if not > 0
        """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    self.__size = size

    def area(self):
        return self._size
