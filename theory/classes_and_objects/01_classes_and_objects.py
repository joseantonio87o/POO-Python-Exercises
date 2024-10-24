# 01_classes_and_objects.py
# ------------------------------------------------------
# Project: POO-Python-Exercises
# Version: 1.2 # Updated to v1.2
# Last Updated: 2024-10-21
# Author: Jose Antonio
# ------------------------------------------------------
# Change Log:
# v1.2 - Translated final comment and updated script version to 1.2
# v1.1 - Translated comments, variable names, and function names to English
# v1.0 - Initial version with basic class structure and comments in Spanish
# ------------------------------------------------------

# Define a Car class with two attributes: brand and model
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute

    # Method to show information about the car
    def show_info(self):
        print(f"This car is a {self.brand} {self.model}")

# Create an instance of the Car object
my_car = Car("Toyota", "Corolla")
my_car.show_info()  # Output: This car is a Toyota Corolla
