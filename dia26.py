"""
    Biienvenidos al dia 26 de #100diasdepython
            El reto de hoy es:
Utiliza la funcion copy() para crear una copia de la lista de compras utilizada 
en el reto anterior, compara sus Id's en memoria e imprime el resultado
"""
lista_compras = ["10 Panes", "1/2 doc. de Huevos", "Leche de soja", "1 doc. de Nucitas"]
copia_lista = lista_compras.copy()
print(id(lista_compras) == id(copia_lista))