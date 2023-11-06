#!/usr/bin/python3
"""Module with simple object attribute lookup function"""


def lookup(obj):
    """gets a list of available attributes and methods of an object"""
    return dir(obj)
