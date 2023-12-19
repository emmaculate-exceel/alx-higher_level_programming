#!/usr/bin/python3
""" Declaration of a class """


class Square:
    """ instantiation of a class """

    def __init__(self, size=0):
        """ size must be an int """

        try:
            if (!int(size)):
                return

            if (size < 0):
                return
        except typeError:
            print("size must be an integer")

        except valueError:
            print("size must be >= 0")
