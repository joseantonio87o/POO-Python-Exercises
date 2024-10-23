# Private and Protected Attributes
# ------------------------------------------------------
# Description: This script discusses private and protected attributes in Python and how to access them.
# Project: POO-Python-Exercises
# Version: 1.0
# Last Updated: 2024-10-23
# Author: Jose Antonio
# ------------------------------------------------------

# Defining the Car class
class Car:
    # The __init__ method is the constructor that initializes the attributes of the Car object
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute, not accessible directly from outside the class
        self.model = model  # Public attribute, accessible from outside the class

    # Public method to access the private attribute 'brand'
    def get_brand(self):
        return self.__brand

# Creating an instance of Car with specific brand and model attributes
car1 = Car("Toyota", "Corolla")

# Accessing the private attribute using the public method 'get_brand'
print(car1.get_brand())  # Output: Toyota

# Attempting to access the private attribute directly would raise an AttributeError
# print(car1.__brand)  # This would raise an error since __brand is private
