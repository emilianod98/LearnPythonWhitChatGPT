'''
24. COMPROBACIÓN DE SI UNA CADENA DE TEXTO ES PALÍNDROMO

Escribir un programa que pida al usuario una cadena de texto y determine si es un palíndromo o no. Una cadena es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda. El programa debe mostrar en pantalla un mensaje indicando si la cadena es palíndromo o no.
'''

# Pedimos al usuario que ingrese una cadena de texto
cadena = input("Ingrese una cadena de texto: ")

# Convertimos el texto a minúsculas
cadena = cadena.lower()

# Invertimos la cadena
cadena_invertida = cadena[::-1]

# Comparamos la cadena original con la invertida
if cadena == cadena_invertida:
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")


# Solución por ChatGPT