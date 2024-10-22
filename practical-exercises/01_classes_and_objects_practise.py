# 01_classes_and_objects_practise.py
# ------------------------------------------------------
# Project: POO-Python-Exercises
# Version: 1.1
# Last Updated: 2024-10-22
# Author: Jose Antonio
# ------------------------------------------------------
# Exercise Description:
# 1. Define a class Person with attributes: name, age, and city.
#    Add a method called saludar() that prints a greeting with the name and city.
#    Add a method called es_mayor_de_edad() that returns True if the person is over 18.
#
# 2. Define a class Book with attributes title and author.
#    Create another class Library that contains a list of books.
#    Add methods to add books to the library and list all the books available.
#
# 3. Define a class Vehicle with attributes brand and model.
#    Create a class Car that inherits from Vehicle and adds an attribute numero_de_puertas.
#    Override the describir() method to include vehicle description and the number of doors.
# ------------------------------------------------------
def exercise_1():
    # Code for Exercise 1
    class Person:
        def __init__(self, name, age, city):
            self.name = name # Instance attribute for name
            self.age = int(age) # Instance attribute for age, converted to integer
            self.city = city # Instance attribute for city

        def saludar(self):
            # Method to print a greeting with the person's name, age, and city
            print(f"Hi, I am {self.name} from {self.city} and I has {self.age} years old.")
        
        def es_mayor_edad(self):
            # Method to check if the person is over 18, under 18, or exactly 18 years old
            if self.age > 18:
                print(f"{self.name} is over 18")
            elif self.age == 18:
                print(f"{self.name} is 18")
            else:
                print(f"{self.name} is under 18")

    # Creating instances of the Person class
    person1 = Person("Jose", "17", "Barcelona")
    person2 = Person("Pablo", "28", "Madrid")
    person3 = Person("Marta", "18", "Caceres")

    # Calling the saludar method for each person
    person1.saludar()
    person2.saludar()
    person3.saludar()

    # Calling the es_mayor_edad method for each person
    person1.es_mayor_edad()
    person2.es_mayor_edad()
    person3.es_mayor_edad()

def exercise_2():
    # Code for Exercise 2
    class Book():
        def __init__(self, tittle, author):
            self.title = tittle
            self.author = author
    
    class Library():
        def __init__(self):
            self.books = []
        
        def add_book(self, book):
            self.books.append(book)
        
        def list_books(self):
            for book in self.books:
                print(f"{book.title} by {book.author}")
    
    book1 = Book("1984","George Orwell")
    book2 = Book("The Catcher in the Rye", "J.D. Salinger")
    book3 = Book("The Lord of the rings", "J.R.R. Tolkien")

    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.list_books()



# def exercise_3():

# To run each exercise:
# exercise_1()
exercise_2()
# exercise_3()