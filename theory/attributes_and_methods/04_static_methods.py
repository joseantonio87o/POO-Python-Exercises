# Static Methods
# ------------------------------------------------------
# Description: This script demonstrates how to define and use static methods in Python.
# Project: POO-Python-Exercises
# Version: 1.0
# Last Updated: 2024-10-23
# Author: Jose Antonio
# ------------------------------------------------------

# Defining the Car class
class Car:
    # Defining a static method using the @staticmethod decorator
    @staticmethod
    def is_motor_vehicle():
        # This method returns True, indicating that a car is a motor vehicle
        # Static methods do not use 'self' or 'cls' because they do not operate on instance or class attributes
        return True

# Calling the static method without creating an instance of the Car class
print(Car.is_motor_vehicle())  # Output: True
