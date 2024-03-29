#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements, padding with 0s if necessary
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    # Return a new tuple with the sums of the first two elements of each input tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
