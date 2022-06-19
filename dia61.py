"""
    Bienvenidos al dia 61 de #100diasdepython
            El reto de hoy es:
Utiliza Rejex para validar que las cadenas de la lista sean totalmente numericas
["20200806", "jun122022", "202204DD", "20221208", "22mar2022"]
Imprime una lista con las cadenas numericas
"""
import re

regex = '^[0-9]+$'
lista_cadenas = ["20200806", "jun122022", "202204DD", "20221208", "22mar2022"]

nueva_lista = list(filter(lambda x: re.search(regex, x), lista_cadenas))
print(nueva_lista)
