#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """
    A class representing a square.

    Attributes:
        size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (float or int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If the size is not a number (float or integer).
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares the area of the square with another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares the area of the square with another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compares the area of the square with another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the square is less than the other square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares the area of the square with another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the square is less than or equal to the other square, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compares the area of the square with another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the square is greater than the other square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares the area of the square with another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the square is greater than or equal to the other square, False otherwise.
        """
        return self.area() >= other.area()
