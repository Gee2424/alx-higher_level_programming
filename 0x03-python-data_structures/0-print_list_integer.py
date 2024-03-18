#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints all integers in a list.

    Args:
        my_list (list): The list of integers to be printed.

    Returns:
        None
    """
    for integer in my_list:
        print("{:d}".format(integer))
    
