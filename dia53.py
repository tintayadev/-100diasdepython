"""
    Bienvenidos al dia 53 de #100diasdepython
            El reto de hoy es:
Crea una funcion que reciba una lista de numeros y devuelva una lista de los numeros al cuadrado
Ejecuta la funcion para la lista [2,3,5,7,11]
Imprime el resultado
"""

def squareValuesList(numbers_list: list):
    return [pow(elem, 2) for elem in numbers_list]

print(squareValuesList([2,3,5,7,11]))