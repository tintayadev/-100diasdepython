"""
    Bienvenidos al dia 95 de #100diasdepython
            El reto de hoy es:
Crea una funcion que use argumentos arbitrarios
para recibir N-numeros y determine cual es el mayor y el menor
y los devuelva en un diccionario en el siguiente formato {"mayor": 5, "menor": -10}
Imprime el resultado
"""
import sys

def mayorMenor(*args):
    mayor = -sys.maxsize - 1
    menor = sys.maxsize
    for num in args:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
    return {"mayor": mayor, "menor": menor}

nums = [2,45,1,7,-12,1,7466, -5683554, 1234, 0, 99999]

print(mayorMenor(*nums))



