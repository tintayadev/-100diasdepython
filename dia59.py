"""
    Bienvenidos al dia 59 de #100diasdepython
            El reto de hoy es:
Utiliza una funcion lambda para ordenar de forma ascendente
lal siguiente lista de tuplas tomando el valor numerico como referencia
[("Quimica", 88), ("Fisica", 90), ("Lenguaje", 97)]
Imprime el resultado
"""

lista_materias = [("Quimica", 88), ("Fisica", 90), ("Lenguaje", 97)]


lista_materias = sorted(lista_materias, key=lambda x: x[1])

print(lista_materias)
