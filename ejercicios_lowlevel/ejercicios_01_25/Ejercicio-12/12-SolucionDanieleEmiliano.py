'''
12. CONVERSIÓN DE MILLAS A KILÓMETROS

Escribir un programa que pida al usuario una distancia en millas y muestre en pantalla la distancia equivalente en kilómetros, utilizando la fórmula `1 milla = 1.60934 kilómetros`
'''

# Creamos la funcion conversordeKilometros
def conversordeKilometros (millas):
    # Convertimos las millas a kilómetros utilizando la fórmula dada
    kilometros = millas * 1.60934
    # Mostramos la distancia en kilómetros por pantalla
    print("La distancia en kilómetros es:", kilometros)

# Pedimos al usuario que ingrese la distancia en millas
millas = float(input("Ingrese la distancia en millas: "))

# Llamamos a la función
conversordeKilometros (millas)


# Solución por Daniele Emiliano.