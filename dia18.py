"""
    Biienvenidos al dia 18 de #100diasdepython
            El reto de hoy es:
Declara una variable de tipo cadena, encuentra el primer
y el ultimo caracter en orden lexografico sin usar ciclos e imprimelos
"""
from gettext import find
from sys import maxunicode

cadena = "python"
primero = min(cadena)
ultimo = max(cadena)
print(primero, ultimo)

