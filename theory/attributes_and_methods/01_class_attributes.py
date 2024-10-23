# Class and Instance Attributes
# ------------------------------------------------------
# Description: This script demonstrates the difference between class attributes and instance attributes in Python.
# Project: POO-Python-Exercises
# Version: 1.0
# Last Updated: 2024-10-23
# Author: Jose Antonio
# ------------------------------------------------------

class Car:
    wheels = 4  # Class attribute, shared by all instances of the class

    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute, unique to each instance
        self.model = model  # Instance attribute, unique to each instance

# Creating instances of the Car class
car1 = Car("Toyota", "Corolla")  # car1 is an instance of Car with brand "Toyota" and model "Corolla"
car2 = Car("Ford", "Mustang")  # car2 is an instance of Car with brand "Ford" and model "Mustang"

# Accessing class attributes
print(car1.wheels)  # Accessing the class attribute 'wheels' through car1, output: 4
print(car2.wheels)  # Accessing the class attribute 'wheels' through car2, output: 4

# Accessing instance attributes
print(car1.brand)  # Accessing the instance attribute 'brand' of car1, output: Toyota
print(car2.model)  # Accessing the instance attribute 'model' of car2, output: Mustang
