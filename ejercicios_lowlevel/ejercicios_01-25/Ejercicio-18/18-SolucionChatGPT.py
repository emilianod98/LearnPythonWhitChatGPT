'''
18. NÚMEROS PERFECTOS

Escribir un programa que muestre en pantalla todos los números perfectos menores o iguales a un número dado por el usuario. Un número es perfecto si la suma de sus divisores (excluyendo el propio número) es igual a ese número. Por ejemplo, el número 6 es perfecto porque sus divisores son 1, 2 y 3, y 1 + 2 + 3 = 6.
'''

# Pedir al usuario un número n.
n = int(input("Ingrese un número: "))
# Iterar a través de los números desde 1 hasta n.
for num in range(1, n+1):
    sum_divisors = 0
    # Para cada número, calcular la suma de sus divisores y compararla con el número original.
    for divisor in range(1, num):
        if num % divisor == 0:
            sum_divisors += divisor
    # Si la suma de divisores es igual al número original, imprimir ese número.
    if sum_divisors == num:
        print(num, "es un número perfecto.")
    else:
        print(num, "no es un número perfecto.")

        
# Solución por ChatGPT