#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.

    Args:
        matrix (list): The input matrix to be rotated.

    Returns:
        None: The function modifies the input matrix in place and doesn't
        return anything.
    """
    # Check if the input is a list
    if type(matrix) != list:
        return

    # Check if the input list is not empty and contains only lists as elements
    if len(matrix) <= 0 or not all(map(lambda x: type(x) == list, matrix)):
        return

    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Check if all rows have the same number of columns
    if not all(map(lambda x: len(x) == cols, matrix)):
        return

    # Initialize variables for traversal
    c, r = 0, rows - 1

    # Iterate through the matrix elements
    for i in range(cols * rows):
        # Check if a new row should be added
        if i % rows == 0:
            matrix.append([])

        # Reset the column index and decrement the row index when necessary
        if r == -1:
            r = rows - 1
            c += 1

        # Append the element at the current (r, c) position to the
        # last row of the matrix
        matrix[-1].append(matrix[r][c])

        # Remove the original element if it's the last column and
        # the row index is valid
        if c == cols - 1 and r >= -1:
            matrix.pop(r)

        # Move to the next element by decrementing the row index
        r -= 1
