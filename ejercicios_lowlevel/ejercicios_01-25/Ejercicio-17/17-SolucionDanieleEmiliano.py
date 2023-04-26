'''
17. NÚMEROS PRIMOS

Escribir un programa que pida al usuario un número y determine si es primo o no. Un número es primo si es divisible únicamente por 1 y por sí mismo. El programa debe mostrar en pantalla un mensaje indicando si el número es primo o no.
'''

# Creamos la funcion esPrimo
def esPrimo (numero):
    if numero % 2 == 0:
        print ('El ', numero, ' no es primo!')
    else:
        print ('El ', numero, ' es primo!')

# Solicita al usuario que ingrese un número.
numero = int(input("Ingresa un número entero positivo: "))

# Llamamos a la función
esPrimo(numero)


# Solución por Daniele Emiliano.