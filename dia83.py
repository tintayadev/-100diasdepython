"""
    Bienvenidos al dia 83 de #100diasdepython
            El reto de hoy es:
Utiliza datetime convertir la fecha "Jul 11 2022 1:30AM"
al formato "2022-07-11 01:30:00"
"""
import datetime

fecha = "Jul 11 2022 1:30AM"

nuevo_formato = datetime.datetime.strptime(fecha, '%b %d %Y %I:%M%p')

print(nuevo_formato)
