#!/usr/bin/python3
"""10-student module """
class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """
        Instantiates a student instance

        Args:
            first_name: (str) first name
            last_name: (str) last name
            age: (int) age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json retrieve a dictionary representation of the Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
