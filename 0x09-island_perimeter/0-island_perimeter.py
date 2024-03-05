#!/usr/bin/python3
"""
0x09. Island Perimeter
"""


def island_perimeter(grid):
    """A function that returns the circumference of
    the island described in the grid.
    """
    perimeter = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 1:
                perimeter += 4
                if row and column > 0 and \
                    grid[row - 1][column] == 1 \
                        or grid[row][column - 1] == 1:
                    perimeter -= 2
    return perimeter
