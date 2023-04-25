'''
11. VOLUMEN DE UNA ESFERA

Escribir un programa que pida al usuario el radio de una esfera y muestre en pantalla el volumen de la esfera, utilizando la fórmula `V = (4/3) * π * r^3`. Asegúrate de que el programa muestre un valor aproximado de `π` (puedes utilizar el valor 3.14159).
'''

# Pedimos al usuario que ingrese el radio de la esfera
radio = float(input("Ingrese el radio de la esfera: "))

# Definimos el valor de pi
pi = 3.14159

# Calculamos el volumen de la esfera utilizando la fórmula dada
volumen = (4/3) * pi * radio ** 3

# Mostramos el volumen de la esfera por pantalla
print("El volumen de la esfera es:", volumen)


# Solución por ChatGPT