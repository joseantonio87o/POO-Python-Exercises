# Instance Methods
# ------------------------------------------------------
# Description: This script demonstrates how to define and use instance methods in Python.
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

    # Instance method to display information about the car
    def show_info(self):
        # Prints the brand and model of the car instance
        print(f"This car is a {self.brand} {self.model}")

# Creating instances of the Car class with specific brand and model attributes
car1 = Car("Toyota", "Corolla")  # car1 is a Car instance with brand "Toyota" and model "Corolla"
car2 = Car("Ford", "Mustang")  # car2 is a Car instance with brand "Ford" and model "Mustang"

# Calling the instance method 'show_info' on each car instance
car1.show_info()  # Output: This car is a Toyota Corolla
car2.show_info()  # Output: This car is a Ford Mustang
