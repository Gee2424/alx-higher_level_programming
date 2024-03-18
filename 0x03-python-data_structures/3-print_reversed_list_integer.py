#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers in a list in reverse order.

    Args:
        my_list (list): The list of integers to be printed in reverse order.

    Returns:
        None
    """
    if my_list:
        for integer in reversed(my_list):
            print("{:d}".format(integer))
