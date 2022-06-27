"""
    Bienvenidos al dia 68 de #100diasdepython
            El reto de hoy es:
Utiliza Regex para cambiar el formato de las fechas
de YYYY-MM-DD a DDMMYYYY de las fechas de la lista
["2022-12-05", "1993-06-12", "2005-01-26", "2021-10-08"]
Imprime una lista con las fechas con el nuevo formato
"""
import re

lista_fechas = ["2022-12-05", "1993-06-12", "2005-01-26", "2021-10-08"]

validos = [re.sub("(\d{4})-(\d{1,2})-(\d{1,2})", "\\3\\2\\1", elem) for elem in lista_fechas]

print(validos)
