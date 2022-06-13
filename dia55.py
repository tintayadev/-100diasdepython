"""
    Bienvenidos al dia 55 de #100diasdepython
            El reto de hoy es:
Crea una funcion recursiva para hacer una cuenta regresiva
La funcion tiene como parametro de entrada un numero 
Ejecuta la funcion para el numero 5
Imprime el valor de la cuenta en cada iteracion
"""

def cuentaRegresiva(n: int):
    print(n)
    if n > 0:
        cuentaRegresiva(n-1)
        
cuentaRegresiva(5)