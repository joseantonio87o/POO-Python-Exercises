# Attributes and Methods in OOP - Exercises
# ------------------------------------------------------
# Project: OOP-Python-Exercises
# Version: 1.0
# Last Updated: 2024-10-23
# Author: Jose Antonio
# ------------------------------------------------------
# Description: This script contains multiple exercises to reinforce the concepts of attributes and methods
# in Object-Oriented Programming (OOP). The exercises include examples of class and instance attributes,
# instance methods, class methods, static methods, encapsulation, and other related concepts.

# Exercise 1: Class and Instance Attributes

def Exercise_1():
    class Perro:
        especie = "Canis familiaris"
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad
        # Crear instancias de Perro
    perro1 = Perro("Toby", 4)
    perro2 = Perro("Luna", 2)
    print(f"{perro1.nombre}, {perro1.especie}, Edad: {perro1.edad}")
    print(f"{perro2.nombre}, {perro2.especie}, Edad: {perro2.edad}")

        # Modificar atributo de instancia
    perro1.edad = 5
    print(f"La nueva edad de {perro1.nombre} es {perro1.edad}\n")

# Ejercicio 2: Métodos de Instancia



Exercise_1()