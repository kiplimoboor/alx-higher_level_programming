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
        for j in range(i):
            try:
                row.append(prev_row[j] + prev_row[j + 1])
            except IndexError:
                row.append(prev_row[j] + prev_row[0])

        row.append(1)

        triangle.append(row)

    return triangle
