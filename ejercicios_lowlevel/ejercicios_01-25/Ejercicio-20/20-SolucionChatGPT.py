'''
20. NÚMEROS ABUNDANTES

Escribir un programa que pida al usuario un número y determine si es abundante o no. Un número es abundante si la suma de sus divisores (excluyendo el propio número) es mayor que el número. El programa debe mostrar en pantalla un mensaje indicando si el número es abundante o no.
'''

# Pedimos al usuario que ingrese un número.
numero = int(input("Ingrese un número: "))

# Calculamos la suma de los divisores propios del número.
suma_divisores = 0
for i in range(1, numero):
    if numero % i == 0:
        suma_divisores += i

# Verificamos si el número es abundante o no.
if suma_divisores > numero:
    print("El número es abundante")
else:
    print("El número no es abundante")


# Solución por ChatGPT