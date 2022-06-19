"""
    Bienvenidos al dia 60 de #100diasdepython
            El reto de hoy es:
Utiliza una funcion lambda para capitalizar las palabras de la 
siguiente lista 
["llevo", "sesenta", "dias", "programando", "wiii"]
Imprime el resultado en una nueva lista
"""

lista_palabras = ["llevo", "sesenta", "dias", "programando", "wiii"]

nueva_lista = list(map(lambda x: x.capitalize(), lista_palabras))

print(nueva_lista)
