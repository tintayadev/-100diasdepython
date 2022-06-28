"""
    Bienvenidos al dia 70 de #100diasdepython
            El reto de hoy es:
Utiliza Regex para extraer todas las palabras que 
contengan al menos una 'a' en la siguiente cadena
'Llevas programando 70 dias seguidos'
Imprime una lista con las palabras extraidas
"""
import re

pattern = "^[a-zA-Z0-9]*$"
cadena = 'Llevas programando 70 dias seguidos'

validos = re.findall("[a-zA-Z0-9]*a[a-zA-Z0-9]*", cadena)

print(validos)
