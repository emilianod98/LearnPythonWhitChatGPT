'''
17. NÚMEROS PRIMOS

Escribir un programa que pida al usuario un número y determine si es primo o no. Un número es primo si es divisible únicamente por 1 y por sí mismo. El programa debe mostrar en pantalla un mensaje indicando si el número es primo o no.
'''

# Solicita al usuario que ingrese un número.
numero = int(input("Ingresa un número entero positivo: "))

# Un número primo es aquel que es divisible únicamente por 1 y por sí mismo
# Comenzamos con el supuesto de que el número es primo
es_primo = True

# Verificamos si el número es divisible por algún número entre 2 y el número - 1
for i in range(2, numero):
    if numero % i == 0:
        # Si es divisible, entonces el número no es primo
        es_primo = False
        break

# Mostramos el resultado
if es_primo:
    print(numero, "es un número primo")
else:
    print(numero, "no es un número primo")


# Solución por ChatGPT