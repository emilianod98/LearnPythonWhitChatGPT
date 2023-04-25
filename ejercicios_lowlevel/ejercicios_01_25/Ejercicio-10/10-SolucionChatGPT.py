'''
10. ÁREA DE UN CÍRCULO

Escribir un programa que pida al usuario el radio de un círculo y muestre en pantalla el área del círculo, utilizando la fórmula `A = π * r^2`. Asegúrate de que el programa muestre un valor aproximado de `π` (puedes utilizar el valor 3.14159).
'''

# Pedimos al usuario que ingrese el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Definimos el valor de pi
pi = 3.14159

# Calculamos el área del círculo utilizando la fórmula dada
area = pi * radio ** 2

# Mostramos el área del círculo por pantalla
print("El área del círculo es:", area)


# Solución por ChatGPT