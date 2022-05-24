"""
    Biienvenidos al dia 33 de #100diasdepython
            El reto de hoy es:
Declara una cadena que sea un palindromo y verifica que lo sea sin usar 
funciones adicionales. Imprime el resultado
"""
cadena = "oruro"
cadena_inversa = cadena[::-1]
es_palindromo = cadena == cadena_inversa
print(es_palindromo)
