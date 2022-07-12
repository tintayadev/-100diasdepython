"""
    Bienvenidos al dia 84 de #100diasdepython
            El reto de hoy es:
Utiliza el datetime convertir la cadena "12-07-2022"
a timestamp
Imprime el resultado
"""
from datetime import datetime

fecha = "12-07-2022"

nuevo_formato = datetime.timestamp(datetime.strptime(fecha, "%d-%m-%Y"))

print(nuevo_formato)
