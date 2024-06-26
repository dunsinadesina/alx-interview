#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """
    function that returns a list
    of integers representing the
    pascal triangle of n:
        Returns an empty list of n <= 0
        assume n will always be an integer
    """
    triangle = []

    if n <= 0:
        return []
    
    for i in range(n):
        if (i == 0):
            triangle.append([1])
        else:
            row = []
            for j in range(i + 1):
                if (j == 0 or j == 1):
                    row.append(1)
                else:
                    row.append(triangle[i - 1][j - 1] +
                               triangle[i - j][j])
            triangle.append(row)
    
    return (triangle)