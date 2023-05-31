#!/usr/bin/python3
class Square():
    """square class"""
    def __init__(self, size=0):
        """initialization of instance"""
        if type(size) != int:
            """check if size is an integer"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """check if size is non-negative"""
            raise ValueError("size must be >= 0")
        """Assign to private attr"""
        self.__size = size

