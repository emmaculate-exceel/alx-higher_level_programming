#!/usr/bin/python3
""" Defination class object """


class Square:
    """ Definition of class """

        def __init__(self, size=0):
            """ Definition of a class constructor 
            that takes a single argument (size)"""

            self.__size = size
            def set._size(self, size):
                return self._size
            """ Conditional statment for the
            Args:
                size: the size of square defined
            Raises:
                TypeError: size must be an integer
                ValueErrror: if size is less than zero
            """

                if not isinstance(size, int):
                    raise TypeError("size must be an integer")
                if size < 0:
                    raise ValueError("size must be >= 0")

            def area(self):
                return self.area = size ** 2
