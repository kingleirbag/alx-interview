#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a pascal triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        cur_row = [1]
        for j in range(1, i):
            cur_row.append(prev_row[j-1] + prev_row[j])
        cur_row.append(1)
        triangle.append(cur_row)
    return triangle
