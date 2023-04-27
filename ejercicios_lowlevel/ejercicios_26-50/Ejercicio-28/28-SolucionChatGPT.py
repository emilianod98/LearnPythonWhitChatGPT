'''
28. CÁLCULO DEL RANGO DE UNA LISTA DE NÚMEROS

Escribe un programa que calcule y devuelva el rango de una lista de números ingresada por el usuario.
'''

def calcular_rango(lista):
    rango = max(lista) - min(lista)
    return rango

# Pedimos al usuario que ingrese los números separados por espacios
numeros = input("Ingrese los números separados por espacios: ")

# Convertimos los números a una lista de enteros
lista_numeros = [int(num) for num in numeros.split()]

# Llamamos a la función para calcular el rango
rango = calcular_rango(lista_numeros)

# Mostramos el resultado al usuario
print("El rango de la lista es:", rango)


# Solución por ChatGPT