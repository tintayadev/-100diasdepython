"""
    Bienvenidos al dia 58 de #100diasdepython
            El reto de hoy es:
Utiliza una funcion lambda para sumar las sisguientes listas
lista_a = [2, 4, 5], lista_b = [6, 7, 1]
Imprime el resultado en una nueva lista
"""

lista_a = [2, 4, 5]
lista_b = [6, 7, 1]

new_list = list(map(lambda x, y: x+y, lista_a, lista_b))

print(new_list)
