#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Represents a square

    Attributes:
        size (int): size of a side of the square
        position (tuple): position of the square in 2D space
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square

        Args:
            size (int): size of a side of the square
            position (tuple): position of the square in 2D space

        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the square's area

        Returns:
            The area of the square
        """
        return self.size ** 2

    @property
    def size(self):
        """Getter of size

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of size

        Args:
            value (int): size of a side of the square

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints the square

        Returns:
            None
        """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for j in range(self.size):
            print("".join([" " for k in range(self.position[0])]), end="")
            print("".join(["#" for l in range(self.size)]))

    @property
    def position(self):
        """Getter of position

        Returns:
            The position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter of position

        Args:
            value (tuple): position of the square in 2D space

        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

