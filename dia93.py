"""
    Bienvenidos al dia 93 de #100diasdepython
            El reto de hoy es:
Crea una funcion que use yield y genere los primeros 
10 numeros de la serie Fibonacci
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
Imprime el resultado en una lista
"""
def fibo(num):
    a = 1
    b = 1
    for x in range(num):
        yield a
        a, b = b, a + b
        
lista = list(fibo(10))
print(lista)



