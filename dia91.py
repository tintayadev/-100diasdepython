"""
    Bienvenidos al dia 91 de #100diasdepython
            El reto de hoy es:
Crea una funcion que devuelva los cuadrado de los primero 10 numeros
enteros inciando en 1 utilzando yields
Imprime el resultado en una lista
"""
def cuadrados():
	for i in range(1,11):
		yield(i*i)

lista = list(cuadrados())
print(lista)



