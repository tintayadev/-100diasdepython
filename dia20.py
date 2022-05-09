"""
    Biienvenidos al dia 20 de #100diasdepython
            El reto de hoy es:
De la siguiente cadena: 'PpYyTtHhOoNnIiSsTtAa'
Separa las mayusculas y minusculas sin usar ciclo en nuevas cadenas
e imprime el resultado en una sola linea
"""
cadena = "PpYyTtHhOoNnIiSsTtAa"
mayusculas = ''.join(filter(str.isupper, cadena)) 
minusculas = ''.join(filter(str.islower, cadena)) 
print(mayusculas, minusculas)