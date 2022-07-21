"""
    Bienvenidos al dia 92 de #100diasdepython
            El reto de hoy es:
Crea una funcion que use yield y genere 
la siguiente serie [1, 2, 3, 2, 1, 2, 3, 2, 1]
Imprime el resultado en una lista
"""
def generador(n):
    for x in range(1, n+1):
        if x == 3 or x== 7:
            yield 3
        elif x%2== 0:
            yield 2
        else:
            yield 1

lista = list(generador(9))
print(lista)



