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

    is_matrix = all(isinstance(row, list) for row in matrix)
    is_number = False
    for row in matrix:
        is_number = all((isinstance(element, int) or isinstance(
            element, float)) for element in row)
        if not is_number:
            break

    if not is_matrix or not is_number:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = list(map(lambda a: round(a / div, 2), row))
        new_matrix.append(new_row)

    return new_matrix
