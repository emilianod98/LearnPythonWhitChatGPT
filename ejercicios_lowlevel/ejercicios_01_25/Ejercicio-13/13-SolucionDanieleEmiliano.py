'''
13. CONVERSIÓN DE KILÓMETROS A MILLAS

Escribir un programa que pida al usuario una distancia en kilómetros y muestre en pantalla la distancia equivalente en millas, utilizando la fórmula `1 kilómetro = 0.621371 millas`.
'''

# Creamos la función conversordeMillas
def conversordeMillas (kilometros):
    # Convertimos los kilómetros a millas utilizando la fórmula dada
    millas = kilometros * 0.621371
    # Mostramos la distancia en millas por pantalla
    print("La distancia en millas es:", millas)

# Pedimos al usuario que ingrese la distancia en kilómetros
kilometros = float(input("Ingrese la distancia en kilómetros: "))

# Llamamos a la función
conversordeMillas (kilometros)


# Solución por Daniele Emiliano.