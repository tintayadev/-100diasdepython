"""
    Bienvenidos al dia 88 de #100diasdepython
            El reto de hoy es:
Utiliza calendar para imprimir la cantidad 
de semanas en cada mes del año 2022
"""
import calendar

lista = [ len(calendar.monthcalendar(2022,elem)) for elem in range(1,13) ]
print(lista)


