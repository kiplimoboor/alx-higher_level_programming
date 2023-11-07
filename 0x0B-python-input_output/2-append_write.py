#!/usr/bin/python3

"""Module that appends into a file"""


def append_write(filename="", text=""):
    """Appends text into filename

    Args:
        filename (str, optional): The file to be appended to. Defaults to "".
        text (str, optional): The text to append. Defaults to "".

    Return:
        Number of characters written
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
