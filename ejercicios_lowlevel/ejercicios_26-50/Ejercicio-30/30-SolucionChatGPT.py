'''
30. CÁLCULO DE LA DESVIACIÓN ESTÁNDAR DE UNA LISTA DE NÚMEROS

Escribe un programa que calcule y devuelva la desviación estándar de una lista de números ingresada por el usuario.
'''

import math

def calcular_desviacion_estandar(lista):
    # Calculamos la media aritmética de la lista
    media = sum(lista) / len(lista)
    
    # Calculamos la suma de los cuadrados de las diferencias
    # entre cada elemento de la lista y la media aritmética
    suma_cuadrados = sum([(x - media) ** 2 for x in lista])
    
    # Calculamos la desviación estándar
    desviacion_estandar = math.sqrt(suma_cuadrados / (len(lista) - 1))
    
    return desviacion_estandar

# Pedimos al usuario que ingrese una lista de números separados por comas
numeros = input("Ingrese una lista de números separados por comas: ")

# Convertimos la cadena de entrada en una lista de números enteros
lista = [int(x) for x in numeros.split(",")]

# Calculamos la desviación estándar de la lista
desviacion_estandar = calcular_desviacion_estandar(lista)

# Mostramos el resultado
print("La desviación estándar de la lista es:", desviacion_estandar)


# Solución por ChatGPT