'''
07. CONVERSIÓN DE GRADOS FAHREHEIT A CELSIUS

Escribir un programa que pida al usuario una temperatura en grados Fahrenheit y muestre en pantalla la temperatura equivalente en grados Celsius, utilizando la fórmula 
°C = (°F - 32) / 1.8.
'''

# Pedimos al usuario que ingrese la temperatura en grados Fahrenheit
fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))

# Convertimos la temperatura a grados Celsius utilizando la fórmula dada
celsius = (fahrenheit - 32) / 1.8

# Mostramos la temperatura en grados Celsius por pantalla
print("La temperatura en grados Celsius es:", celsius)


# Solución por ChatGPT