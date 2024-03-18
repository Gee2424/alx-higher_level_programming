#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]): 
    """
    Prints a matrix of integers.

    Args:
        matrix (list of lists): The matrix to be printed.

    Returns:
        None
    """
    for row in matrix:
        for i, num in enumerate(row):
            print("{:d}".format(num), end="" if i < len(row) - 1 else "\n")
    if not matrix:
        print()
