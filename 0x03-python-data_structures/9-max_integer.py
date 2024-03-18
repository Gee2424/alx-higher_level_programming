#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None
    max_val = my_list[0]  # Initialize max_val with the first element
    for num in my_list:
        if num > max_val:
            max_val = num  # Update max_val if a larger num is found
    return max_val

if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
