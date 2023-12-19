#!/usr/bin/python3
""" Declaration of a class """


class Square:
    """ instantiation of a class """

    def __init__(self, size=0):
        """ Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        try:
            if (!int(size)):
                return

            if (size < 0):
                return
        except typeError:
            print("size must be an integer")

        except valueError:
            print("size must be >= 0")
