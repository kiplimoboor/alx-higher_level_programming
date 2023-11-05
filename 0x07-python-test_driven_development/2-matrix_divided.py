#!/usr/bin/python3
"""Simple matrix division module"""


def matrix_divided(matrix, div):
    """Divides elements of a matrix
    Args:
        matrix(list): The matrix
        div(int/float): The divider

    Returns:
        list: new matrix of same size with divided values

    Raises:
        TypeError: when the matrix parameter isn't a list
                   and when elements of matrix aren't float or int
                   and when div parameter isn't a number

        ZeroDivisionError: when div is 0
    """

    if not isinstance(matrix, list) or matrix == []\
            or not all(isinstance(row, list) for row in matrix)\
            or not all(isinstance(el, int) or isinstance(el, float)
                       for row in matrix for el in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda el: round(el / div, 2), row)) for row in matrix])
