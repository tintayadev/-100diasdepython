"""
    Biienvenidos al dia 40 de #100diasdepython
            El reto de hoy es:
Utiliza el conjunto del reto anterior y elimina al gato del conjunto, si es que existiera
sin usar sentencias condicionales. Imprime el resultado.
"""
animales = {"Pinguino", "Flamenco", "Panda", "Leon", "Serpiente"}
animales.discard("Gato")
print(animales)