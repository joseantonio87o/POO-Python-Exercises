# 01_classes_and_objects.py
# ------------------------------------------------------
# Project: POO-Python-Exercises
# Version: 1.1
# Last Updated: 2024-10-21
# Author: Jose Antonio
# ------------------------------------------------------
# Change Log:
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
        print(f"This car is a {self.marca} {self.modelo}")

# Create an instance of the Car object
mi_coche = Car("Toyota", "Corolla")
mi_coche.show()  # Output: This car is a Toyota Corolla
