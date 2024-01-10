#!/usr/bin/python3
""" A function for reading of files """


def read_file(filename=""):
    """ using a function using the "with" keyword """

    with open(filename, encoding='utf-8') as f:
        x = f.read()
        print(x, end="")
