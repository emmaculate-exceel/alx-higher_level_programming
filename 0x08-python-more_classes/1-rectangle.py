#!/usr/bin/python3
""" A Rectangle class """


class Rectangle:
    """ Private instance width """

    def __init__(self, width):
        """ instantion of width """

        @property
        def width(self):
            """ Getters method to retrieve it """

            return self.__width
        @width.setter
        def width(self, value):
            """ setter method for the width """

            if width is not instanceof(width, int):
                raise TypeError("width must be an integer")
            if width is < 0:
                raise ValueError("width must be >= 0")
    """ private instance height """

    def __init__(self, height):
        """ instation of height """

        @property
        def height(self):
            """ getters method for height """

            return self.__height
        @height.setter
        def height(self, value):
            """ setter for the height method """

            if height is not instanceof(height, int):
                raise TypeError("height must be an integer")
            if height is < 0:
                raise ValueError("height must be >= 0")

        """ instantiation of optional value """

        def __init__(self, width=0, height=0):
            self.width = width
            self.height = height
