"""
    Bienvenidos al dia 86 de #100diasdepython
            El reto de hoy es:
Utiliza el datetime para calcular la cantidad del segundos que han pasado
desde el inicio del reto considerando solo la fecha
Considere que el reto inicio el "20/04/2022" 
Imprime el resultado
"""
from datetime import date, datetime

inicio = datetime.strptime("20/04/2022", "%d/%m/%Y")
dia86 = datetime.strptime("14/07/2022", "%d/%m/%Y")

segundos = (dia86 - inicio).total_seconds()
print(segundos)

