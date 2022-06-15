"""
    Bienvenidos al dia 57 de #100diasdepython
            El reto de hoy es:
Utiliza una funcion lambda para encontrar los multiplos
de 3 en la lista de numeros
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Imprime el resultado de la nueva lista
"""
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(filter(lambda x: x%3 == 0, numbers_list))

print(new_list)
