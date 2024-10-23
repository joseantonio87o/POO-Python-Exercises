# Class Methods
# ------------------------------------------------------
# Description: This script demonstrates how to define and use class methods in Python.
# Project: POO-Python-Exercises
# Version: 1.0
# Last Updated: 2024-10-23
# Author: Jose Antonio
# ------------------------------------------------------

# Defining the Car class
class Car:
    wheels = 4  # Class attribute, shared by all instances of the Car class

    # The __init__ method is the constructor that initializes the attributes of the Car object
    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute 'brand', specific to each instance
        self.model = model  # Instance attribute 'model', specific to each instance

    # Defining a class method using the @classmethod decorator
    @classmethod
    def show_wheels(cls):
        # Prints the value of the class attribute 'wheels'
        # The 'cls' parameter refers to the class itself, not an instance
        print(f"All cars have {cls.wheels} wheels.")

# Calling the class method 'show_wheels' on the Car class
Car.show_wheels()  # Output: All cars have 4 wheels
