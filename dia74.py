"""
    Bienvenidos al dia 71 de #100diasdepython
            El reto de hoy es:
Utiliza itertools para obtener el producto cartesiano
de las siguientes listas
[1, 3, 5] y [2, 4, 6]
Imprime el resultado en una lista de tuplas
"""

import itertools
 
lista_a = [1, 3, 5]
lista_b = [2, 4, 6]

print (list(itertools.product(lista_a, lista_b)))
