"""
    Bienvenidos al dia 100 de #100diasdepython
            El reto de hoy es:
Utiliza try para capturar e imprimir la excepcion 
dentro de la siguiente funcion y agrega un mensaje final utilizando finally
En este reto si se aceptan multiples print
"""

def dia100():
    mensaje = "Llegaste al ultimo dia"
    print(mensaje[len(mensaje)])

try:
    dia100()
except Exception as e:
    print("Error: {}".format(e) )
finally:
    print("Utilizando finally Wii")