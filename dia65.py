"""
    Bienvenidos al dia 65 de #100diasdepython
            El reto de hoy es:
Utiliza Regex para para quita los prefijos telefonicos de los telefonos de la siguiente lista
["+54 11 1234 5678", "+591 68754321", "+56 9 8765 4321"]
Imprime una lista con las IP validas
"""
import re

patron = "\+[0-9]*\s"

telefonos = ["+54 11 1234 5678", "+591 68754321", "+56 9 8765 4321"]

nueva_lista = [re.sub(patron, '', elem) for elem in telefonos]

print(nueva_lista)
