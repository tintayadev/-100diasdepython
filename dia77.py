"""
    Bienvenidos al dia 77 de #100diasdepython
            El reto de hoy es:
Utiliza itertools para obtener los multiplos 
de 5 de la siguiente lista
lista =[1, 5, 10, 23, 3, 555, 11, 10]
Imprime el resultado en una lista
"""

import itertools
 
lista =[1, 5, 10, 23, 3, 555, 11, 10]

result1 = list(itertools.filterfalse(lambda x: x % 5 != 0, lista))

print(result1)


