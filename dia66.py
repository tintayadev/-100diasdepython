"""
    Bienvenidos al dia 66 de #100diasdepython
            El reto de hoy es:
Utiliza Regex para para eliminar los caracteres que no sean alfanumericos en las cadenas de la lista
["Python3.10", "Python3", "ProgramandoAndo", "jun2022", "#100diasdecodigo", "Felicidades!"]
Imprime una lista con las cadenas limpias
"""
import re

patron = "[^0-9A-Za-z]"
lista_cadenas = ["Python3.10", "Python3", "ProgramandoAndo", "jun2022", "#100diasdecodigo", "Felicidades!"]
nueva_lista = [re.sub( patron, "", elem) for elem in lista_cadenas]

print(nueva_lista)