#!/usr/bin/python3
""" Declaration of a class """

    
class Square:
    """ instantiation of a class """

    def __init__(self, size = 0):
        """ size must be an int """
        try:
            if (!int(size) and size < 0):

        except valueError:
            print("size must be >= 0")
                    
        except typeError:
            print("size must be an integer")
