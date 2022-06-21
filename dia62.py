"""
    Bienvenidos al dia 62 de #100diasdepython
            El reto de hoy es:
Utiliza Rejex para validar que las cadenas de la lista de emails
["pythonlapaz@gmail.com", "dias.com",
 "comidita@.com", "programando@outlook.com"]
Imprime una lista con los emails validos
"""
import re

patron = '\S+@\S+\.\S'
lista_cadenas = ["pythonlapaz@gmail.com", "dias.com", "comidita@.com", "programando@outlook.com"]

nueva_lista = [elem for elem in lista_cadenas if re.search(patron, elem)]
print(nueva_lista)
