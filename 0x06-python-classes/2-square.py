#!/usr/bin/python3
class Square():
    """square class"""
    def __init__(self, size=0):
        """initialization of instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """Assign to private attr"""
        self.__size = size

