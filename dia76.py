"""
    Bienvenidos al dia 76 de #100diasdepython
            El reto de hoy es:
Utiliza itertools para obtener el valor
máximo de cada tupla de la siguiente lista
lista = [(2, 4, 6), (7, 8, 5, 6), (5, 10)]
Imprime el resultado en una lista
"""

import itertools
 
lista = [(2, 4, 6), (7, 8, 5, 6), (5, 10)]


result1 = list(itertools.starmap(max, lista))

print(result1)


