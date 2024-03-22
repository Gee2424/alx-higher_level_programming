#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix: A 2 dimensional array (list of lists) of integers.

    Returns:
        A new matrix where each value is the square of the value of the input matrix.
    """
    # Check if the input is a matrix (list of lists)
    if not matrix or not all(isinstance(row, list) for row in matrix):
        return None

    # Create a new matrix with squared values using list comprehension
    new_matrix = [[x**2 for x in row] for row in matrix]

    return new_matrix
