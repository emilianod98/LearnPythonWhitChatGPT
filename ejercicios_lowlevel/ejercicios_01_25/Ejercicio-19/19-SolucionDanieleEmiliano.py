'''
19. NÚMEROS AMISTOSOS

Escribir un programa que pida al usuario un número y muestre en pantalla todos los pares de números amistosos menores o iguales a ese número. Dos números son amistosos si la suma de los divisores propios (excluyendo el propio número) de cada uno es igual al otro número. Por ejemplo, los números 220 y 284 son amistosos porque los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110, que suman 284, y los divisores propios de 284 son 1, 2, 4, 71 y 142, que suman 220.
'''



# Función que calcula la suma de los divisores propios de un número.
def sum_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

# Función que encuentra los pares de números amistosos menores o iguales a un número dado.
def find_amicable_numbers(limit):
    amicable_pairs = []
    for i in range(1, limit+1):
        sum_i = sum_divisors(i)
        if sum_i > i:
            sum_j = sum_divisors(sum_i)
            if sum_j == i:
                amicable_pairs.append((i, sum_i))
    return amicable_pairs

# Pedimos al usuario que ingrese un número límite
limite = int(input("Ingrese un número límite: "))
pares_amistosos = find_amicable_numbers(limite)

# Imprimimos los pares amistosos encontrados
if len(pares_amistosos) == 0:
    print("No se encontraron pares amistosos.")
else:
    print("Los siguientes son pares amistosos:")
    for par in pares_amistosos:
        print(par)



# Solución por Daniele Emiliano.