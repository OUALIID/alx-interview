#!/usr/bin/python3
"""Create a function Pascal triangle
"""


def pascal_triangle(n):
    """
    The function returns a list of lists of integers
    representing Pascal's triangle
    """
    triangle = []
    for line in range(n):
        row = [1] * (line + 1)
        triangle.append(row)
    for line in range(2, n):
        for i in range(1, line):
            triangle[line][i] = triangle[
                line - 1][i - 1] + triangle[line - 1][i]
    return triangle
