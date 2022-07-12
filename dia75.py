"""
    Bienvenidos al dia 75 de #100diasdepython
            El reto de hoy es:
Utiliå itertools para obtener el mensaje secreto
en l siguiente cadena "P1y2t3h4o5n6!7"
Imprime el resultado en una cadena
"""

import itertools
 
cadena = "P1y2t3h4o5n6!7"
pista = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

print("".join(list(itertools.compress(cadena, pista))))


