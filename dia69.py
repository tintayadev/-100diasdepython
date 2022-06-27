"""
    Bienvenidos al dia 69 de #100diasdepython
            El reto de hoy es:
Utiliza Regex para extraer todas las 'a' seguidas de una o mas 
'b's de la siguiente cadena
cadena = "abholaaaaabaaabbpythonistaaaaaabbbbb"
Imprime una lista con las subcadenas extraidas
"""
import re

cadena = "abholaaaaabaaabbpythonistaaaaaabbbbb"

validos = re.findall("a+b", cadena)

print(validos)


