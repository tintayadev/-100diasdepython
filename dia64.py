"""
    Bienvenidos al dia 64 de #100diasdepython
            El reto de hoy es:
Utiliza Regex para quitar los ceros innecesarios de las direcciones IP de la ista
["192.08.001.5", "10.120.023.001", "192.160.2.1"]
Imprime una lista con las IP validas
"""
import re

patron = "^0+(?!$)"

lista = ["192.08.001.5", "10.120.023.001", "192.160.2.1"]
nueva_lista = []

for elem in lista:
    cadena = '.'.join([re.sub(patron, '', x) for x in elem.split('.')])
    nueva_lista.append(cadena)

print(nueva_lista)
