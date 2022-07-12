"""
    Bienvenidos al dia 81 de #100diasdepython
            El reto de hoy es:
Utiliza datetime para agregarle a la fecha actual 7 dias mas
Imprime el resultado
"""
import datetime

hoy = datetime.date.today() + datetime.timedelta(7)
print(hoy)