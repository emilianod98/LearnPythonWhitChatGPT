'''
19. NÚMEROS AMISTOSOS

Escribir un programa que pida al usuario un número y muestre en pantalla todos los pares de números amistosos menores o iguales a ese número. Dos números son amistosos si la suma de los divisores propios (excluyendo el propio número) de cada uno es igual al otro número. Por ejemplo, los números 220 y 284 son amistosos porque los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110, que suman 284, y los divisores propios de 284 son 1, 2, 4, 71 y 142, que suman 220.
'''

def sum_divisores(n):
    """
    Esta función recibe un número n y devuelve la suma de sus divisores propios.
    """
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def amistosos(numero):
    """
    Esta función recibe un número y muestra en pantalla todos los pares de números amistosos menores o iguales a ese número.
    """
    for i in range(1, numero+1):
        for j in range(i+1, numero+1):
            if sum_divisores(i) == j and sum_divisores(j) == i:
                print(i, "y", j, "son amistosos")

# Pedimos al usuario que ingrese un número
num = int(input("Ingrese un número: "))
# Llamamos a la función amistosos
amistosos(num)


# Solución por ChatGPT