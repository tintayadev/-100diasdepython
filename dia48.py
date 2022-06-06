"""
    Bienvenidos al dia 48 de #100diasdepython
            El reto de hoy es:
Con un rango de 5 numeros crea una lista que refleje
con valores booleanos cuales son pares e imprime el resultado
"""
numbers = list(range(3, 8))
print(numbers)
even_numbers = []
for elem in numbers:
    if elem % 2 == 0:
        even_numbers.append(True)
    else:
        even_numbers.append(False)
print(even_numbers)
