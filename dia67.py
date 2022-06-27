"""
    Bienvenidos al dia 67 de #100diasdepython
            El reto de hoy es:
Utiliza Regex para cambiar el formato de las fechas
de YYYYMMDD a de las fechas de la lista
["20221205", "19930612", "20050126", "20211008"]
Imprime una lista con las fechas con el nuevo formato
"""
import re

lista_fechas = ["20221205", "19930612", "20050126", "20211008"]

validos = [re.sub("(\d{4})(\d{1,2})(\d{1,2})", "\\1-\\2-\\3", elem) for elem in lista_fechas]

print(validos)




