"""
    Bienvenidos al dia 79 de #100diasdepython
            El reto de hoy es:
Utiliza itertools para obtener los elementos de la siguiente lista
hasta que alguno contenga un "0"
[2, 3, 5, 7, 13, 103, 25, 15, 45]
Imprime el resultado en una lista
"""

import itertools

def should_drop(x):
    return not(str(x).count('0') > 0)

lista = [2, 3, 5, 7, 13, 103, 25, 15, 45]
resultado = []
for i in itertools.dropwhile(should_drop, lista):
    resultado.append(i)
    
print(resultado)