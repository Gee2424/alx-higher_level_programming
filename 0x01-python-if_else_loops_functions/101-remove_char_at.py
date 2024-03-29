#!/usr/bin/python3

def remove_char_at(str, n):
    """Creates a copy of the string without the character at position n."""
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    return new_str


if __name__ == "__main__":
    # Test cases
    print(remove_char_at("Best School", 3))
    print(remove_char_at("Chicago", 2))
    print(remove_char_at("C is fun!", 0))
    print(remove_char_at("School", 10))
    print(remove_char_at("Python", -2))
