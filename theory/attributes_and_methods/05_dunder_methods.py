# Special Methods (Dunder Methods)
# ------------------------------------------------------
# Description: This script introduces special methods like __str__ and __repr__ in Python.
# Project: POO-Python-Exercises
# Version: 1.0
# Last Updated: 2024-10-23
# Author: Jose Antonio
# ------------------------------------------------------

# Defining the Car class
class Car:
    # The __init__ method is the constructor that initializes the attributes of the Car object
    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute 'brand', specific to each instance
        self.model = model  # Instance attribute 'model', specific to each instance

    # The __str__ method returns a human-readable string representation of the object
    def __str__(self):
        return f"{self.brand} {self.model}"

# Creating an instance of Car with specific brand and model attributes
car1 = Car("Renault", "Captur")
car2 = Car("Toyota", "Corolla")

# The __str__ method is called when we use print() to provide a readable string representation of the object
print(car1)  # Output: Renault Captur
print(car2)  # Output: Toyota Corolla
