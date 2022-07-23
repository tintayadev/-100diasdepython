"""
    Bienvenidos al dia 94 de #100diasdepython
            El reto de hoy es:
Crea una funcion que use argumentos arbitrarios
para recibir N-cadenas de nombres y devuelva una lista de N-sueldos
ejemplo de salida['Hola Katty', 'Hola Ariel']
Imprime el resultado en una lista
"""
def saludando(*args):
    return [ ('Hola '+elem) for elem in args ]

nombres = ['Cris', 'Feli', 'Laiz', 'Keylen', 'Marco', 'Hugo', 'Zaida', 'Armando', 'Antonio', 'Laura', 'Angela']
saludos = saludando(*nombres)
print(saludos)



