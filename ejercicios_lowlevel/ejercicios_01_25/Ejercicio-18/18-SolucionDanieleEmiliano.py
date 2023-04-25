'''
18. NÚMEROS PERFECTOS

Escribir un programa que muestre en pantalla todos los números perfectos menores o iguales a un número dado por el usuario. Un número es perfecto si la suma de sus divisores (excluyendo el propio número) es igual a ese número. Por ejemplo, el número 6 es perfecto porque sus divisores son 1, 2 y 3, y 1 + 2 + 3 = 6.
'''

# Creamos una función llamada numeroPerfecto.
def numeroPerfecto(numero):
    # Vamos a iterar a través de los números.
    for n in range(1, numero + 1):
        # Inicializamos una variable llamada divisor.
        divisor = 0
        # Iteramos a través de los posibles divisores.
        for i in range(1, n):
            # Si el número es divisible por i, lo sumamos a divisor.
            if n % i == 0:
                divisor += i
        # Si divisor es igual a n, n es un número perfecto.
        if divisor == n:
            print(n, "es un número perfecto.")
        else:
            print(n, "no es un número perfecto.")

# Pedimos al usuario que ingrese un número.
numero = int(input('Ingrese un número: '))

# Llamamos a la funcíon 
numeroPerfecto(numero)


# Solución por Daniele Emiliano.