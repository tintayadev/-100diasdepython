"""
    Biienvenidos al dia 12 de #100diasdepython
            El reto de hoy es:
Intercambia el valor de dos variables e imprime su 
    en memoria utilizando la funcion id()
"""
num = 10
cadena = "diez"

num, cadena = cadena, num

print(id(cadena), id(num))