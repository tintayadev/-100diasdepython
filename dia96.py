"""
    Bienvenidos al dia 96 de #100diasdepython
            El reto de hoy es:
Crea una funcion que use argumentos arbitrarios
de tipo keyword para recibir nombre, apellido, y edad y
devuelva estos argumentos en un diccionario en el siguiente formato
{"nombre": "Pepito", "apellido": "Perez", "edad": 25}
Imprime el resultado
"""


def mayorMenor(*kws):
    return {"nombre": kws[0], "apellido": kws[1], "edad": kws[2]}

datos = ["Pepito", "Perez", 25]

print(mayorMenor(*datos))



