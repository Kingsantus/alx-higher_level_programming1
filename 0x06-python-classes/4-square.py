#!/usr/bin/python3
"""square module"""
class Square():
    """Square class"""
    def __init__(self, size=0):
        """initialization of attr"""
        self.size = size

    @property
    def size(self):
        """get metthod for the size attr"""
        return self.__size

    @size.setter
    def size(self, value):
        """set method for size attr"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """Assign to private attr"""
        self.__size = size

    def area(self):
        """public instance to return square"""
        return self.__size ** 2
