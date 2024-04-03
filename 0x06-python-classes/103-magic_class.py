#!/usr/bin/python3
import math

class MagicClass:
    """
    A class that performs magic operations.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance.

        Args:
            radius (int or float, optional): The radius of the magic object. Defaults to 0.

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the magic object.

        Returns:
            float: The area of the magic object.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the magic object.

        Returns:
            float: The circumference of the magic object.
        """
        return 2 * math.pi * self.__radius
