"""
    Bienvenidos al dia 54 de #100diasdepython
            El reto de hoy es:
Crea una funcion que reciba una lista de cadenas y devuelva un diccinoario
con la cantidad de vocales de cada cadena
Ejemplo de entrada:['Python', 'es', 'cool']
Ejemplo de salida: ['Python': 1, 'es': 1, 'cool': 2]
Imprime el resultado
"""

def procedureList(cadenas: list):
    dic_vocales = {}
    for elem in cadenas:
        dic_vocales[elem] = elem.count('a')+ elem.count('e')+ elem.count('i')+ elem.count('o')+ elem.count('u')
    return dic_vocales
lista_cadenas = ['Python', 'es', 'cool']
print(procedureList(lista_cadenas))