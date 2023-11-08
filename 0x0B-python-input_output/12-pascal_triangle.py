#!/usr/bin/python3
"""Module for Pascal Triangle"""


def pascal_triangle(n):
    """Returns a pascal triangle of size n

    Args:
        n (int): Size of the triangle
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(n - 1):
        prev_row = triangle[i]
        row = [1]
        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])
        row.append(1)
        triangle.append(row)
    return triangle
