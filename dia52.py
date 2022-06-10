"""
    Bienvenidos al dia 52 de #100diasdepython
            El reto de hoy es:
Crea una funcion que convierta un numero enterio en binario sin usar la funcion bin()
El paramentro de entrada es un numero entero
El valor de salida es una cadena del valor del numero binario
Ejecuta la funcion para el numero 52
Imprime el resultado
"""

def integerToBinary(n: int):
    n_binary = ""
    while n != 0:
        n_binary = str(n % 2) + n_binary
        n = n // 2
    return n_binary

print(integerToBinary(52))