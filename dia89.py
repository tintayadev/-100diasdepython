"""
    Bienvenidos al dia 89 de #100diasdepython
            El reto de hoy es:
Utiliza calendar par aobtener los dias lunes del mes de Julio del año 2022
Imprimer el resultado en una lista
"""
from calendar import monthcalendar

lunes = [ s[0] for s in monthcalendar(2022, 7) if s[0] != 0 ]

print(lunes)




