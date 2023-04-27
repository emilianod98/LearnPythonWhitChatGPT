'''
27. CÁLCULO DE LA MODA DE UNA LISTA DE NÚMEROS

Escribe un programa que calcule y devuelva la moda de una lista de números ingresada por el usuario.
'''
# El módulo collections de Python, que incluye una clase Counter que puede ser útil para contar la frecuencia de los elementos en una lista.
from collections import Counter

# Creamos una función llamada calcularModa
def calcularModa(lista):
    frecuencias = Counter(lista)
    moda = max(dict(frecuencias), key=frecuencias.get)
    modas = [valor for valor, frecuencia in frecuencias.items() if frecuencia == frecuencias[moda]]
    return print ('La/s moda/s es/son: ', modas)


# Se pide al usuario que ingrese una lista de números separados por comas.
numeros = input("Ingrese una lista de números separados por comas: ")

# Convertimos la cadena de entrada en una lista de números enteros.
lista = [int(numero) for numero in numeros.split(",")]

# Llamamos a la función
calcularModa(lista)


# Solución por Daniele Emiliano.