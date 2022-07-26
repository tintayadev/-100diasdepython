"""
    Bienvenidos al dia 97 de #100diasdepython
            El reto de hoy es:
Crea una funcion que use argumentos arbitrarios
de tipo keyword para recibir los 3 lados 
de un triangulo y calcule su perimetro
Imprime el resultado en un numero de punto flotante
"""

def perimetro(**args):
    result = 0.0
    for elem in args.values():
        result = result + float(elem)
    return result

print(perimetro(lado_a = 13, lado_b = 10, lado_c = 12))