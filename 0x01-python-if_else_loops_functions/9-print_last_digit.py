#!/usr/bin/python3

def print_last_digit(number):
    """Prints and returns the last digit of a number."""
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit

if __name__ == "__main__":

    print_last_digit(98)
    print()
    print_last_digit(0)
    print()
    r = print_last_digit(-1024)
    print()
    print(r)
