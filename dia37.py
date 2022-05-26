"""
    Biienvenidos al dia 37 de #100diasdepython
            El reto de hoy es:
Utiliza el diccionario de palabras del anterior reto para eliminar todos 
elementos en el diccionario sin usar ciclos, imprime el resultado
"""
dic = {
    "Python" : "Lenguaje de alto nivel de programacion interpretado",
    "Javascript" : "Lenguaje de programacion interpretado que usa el standar ECMAScript",
    "Java" : "Java es un lenguaje de programación orientado a objetos que permite el desarrollo de aplicaciones de manera fácil y sencilla" ,
    "Kotlin" : "Kotlin es un lenguaje de programación de tipado estático que corre sobre la máquina virtual de Java y que también puede ser compilado a código fuente de JavaScript.",
    "Dart" : "Dart es un lenguaje de programación de código abierto, desarrollado por Google."
}
dic.clear()
print(dic)
