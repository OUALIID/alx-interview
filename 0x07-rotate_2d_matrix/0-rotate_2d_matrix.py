#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    matrix[:] = zip(*matrix[::-1])
