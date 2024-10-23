# Dynamic Attributes and Methods
# ------------------------------------------------------
# Description: This script demonstrates how to add attributes and methods dynamically to objects in Python.
# Project: POO-Python-Exercises
# Version: 1.0
# Last Updated: 2024-10-23
# Author: Jose Antonio
# ------------------------------------------------------

# Defining the Car class
class Car:
    # The __init__ method initializes the attributes of the Car object
    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute 'brand', specific to each instance
        self.model = model  # Instance attribute 'model', specific to each instance

# Creating an instance of the Car class with specific brand and model attributes
car1 = Car("Toyota", "Corolla")

# Adding an attribute dynamically to the car1 instance
car1.color = "Red"  # Adding a new attribute 'color' to car1
print(car1.color)  # Output: Red

# Defining a function to be added dynamically as a method
def start(self):
    # This method prints a message indicating that the car has started
    print(f"The {self.brand} {self.model} has started.")

# Adding the 'start' function as a method to the Car class dynamically
Car.start = start

# Calling the dynamically added method on the car1 instance
car1.start()  # Output: The Toyota Corolla has started
