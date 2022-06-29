"""
    Bienvenidos al dia 71 de #100diasdepython
            El reto de hoy es:
Utiliza itertools para generar una serie de sumas 
acumuladas con los numeros de la siguiente lista
lista = [0, 1, 1, 2, 3, 5, 8]
Imprime el resultado
"""

import itertools
 
lista = [0, 1, 1, 2, 3, 5, 8]

print (list(itertools.accumulate(lista)))