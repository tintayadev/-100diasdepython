"""
    Bienvenidos al dia 55 de #100diasdepython
            El reto de hoy es:
Utiliza una funcion lambda para encontrar la raiz cuadrada de esta lista
de numeros [49, 4, 36, 16, 25]
Imprime el resultado en una nueva lista
"""

import math

numbers_list = [49, 4, 36, 16, 25]

raices = lambda lista: [int(math.sqrt(elem)) for elem in lista]

nueva_lista = raices(numbers_list)
print(nueva_lista)