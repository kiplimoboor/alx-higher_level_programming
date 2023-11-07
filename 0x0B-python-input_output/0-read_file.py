#!/usr/bin/python3
"""Module that reads a file"""


def read_file(filename=""):
    """Reads a file and prints ot to stdout

    Args:
        filename (str, optional): The name of the file. Defaults to "".
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read())
