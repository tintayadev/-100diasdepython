"""
    Bienvenidos al dia 78 de #100diasdepython
            El reto de hoy es:
Utiliza itertools para unir las siguientes tuplas
(78, 100) ("Dias", "Python")
Obten el tipo de cada dato e imprimelo en una lista
"""

import itertools
 
tupla = tuple(itertools.chain((78, 100), ("Dias", "Python")))

lista = [type(elem) for elem in tupla]

print(lista)