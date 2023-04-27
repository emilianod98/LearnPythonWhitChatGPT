'''
30. CÁLCULO DE LA DESVIACIÓN ESTÁNDAR DE UNA LISTA DE NÚMEROS

Escribe un programa que calcule y devuelva la desviación estándar de una lista de números ingresada por el usuario.
'''

# Importamos la libreria math
import math
# Creamos una una función llamada desviacionEstandar
def desviacionEstandar (lista):
    # Creamos una variable donde vamos a almacenar la media de la lista.
    media = sum(lista) / len(lista)
    # Calculamos la suma de los cuadrados de las deviaciones respecto a la media
    sumaCuadrados = sum((x - media)**2 for x in lista)
    # Calculamos la desviación estándar como la raíz cuadrada de la varianza
    varianza = sumaCuadrados / (len(lista) - 1)
    desviacion = math.sqrt(varianza)
    # Mostramos el resultado por pantalla
    return print("La desviación estándar de la lista es:", desviacion)


# Pedimos al usuario que ingrese una lista de números separados por comas
numeros = input("Ingrese una lista de números separados por comas: ")

# Convertimos la cadena de entrada en una lista de números enteros
lista = [int(numero) for numero in numeros.split(",")]

# Llamamos a al función
desviacionEstandar(lista)


# Solución por Daniele Emiliano.