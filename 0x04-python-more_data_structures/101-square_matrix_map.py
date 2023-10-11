#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda x: list(y ** 2 for y in x)), matrix))
