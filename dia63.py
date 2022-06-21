"""
    Bienvenidos al dia 63 de #100diasdepython
            El reto de hoy es:
Utiliza Rejex para validar que las cadenas solo contengan caracteres alfanumericos
["Python3.10", "Python3", "ProgramandoAndo", "jun2022",
 "#100diasdecodigo", "Felicidades!"]
Imprime una lista con las cadenas validas
"""
import re

patron = "^[a-zA-Z0-9]*$"
lista_cadenas = ["Python3.10", "Python3", "ProgramandoAndo", "jun2022", "#100diasdecodigo", "Felicidades!"]

nueva_lista = [elem for elem in lista_cadenas if re.search(patron, elem)]
print(nueva_lista)
