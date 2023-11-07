#!/usr/bin/python3

"""Module that writes into a file"""


def write_file(filename="", text=""):
    """Writes text into filename

    Args:
        filename (str, optional): The file to be written to. Defaults to "".
        text (str, optional): The text to write. Defaults to "".

    Return:
        Number of characters written
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
