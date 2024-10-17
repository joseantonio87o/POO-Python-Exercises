# 01_classes_and_objects.py

# Definimos una clase Coche con dos atributos: marca y modelo
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo de instancia
        self.modelo = modelo  # Atributo de instancia

    # Método para mostrar información del coche
    def mostrar_info(self):
        print(f"Este coche es un {self.marca} {self.modelo}")

# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla")
mi_coche.mostrar_info()  # Output: Este coche es un Toyota Corolla
