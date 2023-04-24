'''
06. CONVERSIÓN DE GRADOS CELSIUS O FAHRENHEIT

Escribir un programa que pida al usuario una temperatura en grados Celsius y muestre en pantalla la temperatura equivalente en grados Fahrenheit, utilizando la fórmula 
°F = °C * 1.8 + 32.
'''

def convertorCelsiusFahrenheit (celsius):
    fahrenheit = celsius * 1.8 + 32
    # Mostramos la temperatura en grados Fahrenheit por pantalla
    print("La temperatura en grados Fahrenheit es:", fahrenheit)


# Pedimos al usuario que ingrese la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))


# Llamar a la función convertorCelsiusFahrenheit.
convertorCelsiusFahrenheit(celsius)


#Confirmar, que termino de ejecutarse.
print("Programa terminado.")


# Solución por Daniele Emiliano.