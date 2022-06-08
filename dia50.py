"""
    Bienvenidos al dia 50 de #100diasdepython
            El reto de hoy es:
Genera 5 numeros enteros de forma aleatoria
ALmacenalos en una lista
Sumalos e imprime el resultado
"""
import random

random_numbers_list = [int(random.random()*100) for i in range(5)]
sum = 0
for elem in random_numbers_list:
    sum += elem
print(sum)
