#!/usr/bin/python3
"""
    This module returns the list of available attributes
    of an object
"""


def lookup(obj):
    """ Returns a list of object """

    return(dir(obj))
