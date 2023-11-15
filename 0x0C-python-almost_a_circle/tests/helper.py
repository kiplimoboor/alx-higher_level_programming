import io
import sys


def print_io(obj, method="print"):
    """prints to StringIO

    Args:
        rectangle (object): rectangle to be printed
        method (str, optional): Method to invoke. Defaults to "print".

    Returns:
        string: printed output
    """
    output = io.StringIO()
    sys.stdout = output
    if method == "print":
        print(obj)
    else:
        obj.display()
    sys.stdout = sys.__stdout__
    return output.getvalue()
