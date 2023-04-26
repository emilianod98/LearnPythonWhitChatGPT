'''
09. ÁREA DE UN RECTÁNGULO

Escribir un programa que pida al usuario la base y la altura de un rectángulo y muestre en pantalla el área del rectángulo, utilizando la fórmula A = b * h.
'''

#Creamos la función areaRectangulo
def areaRectangulo (base, altura):
    # Calculamos el área del rectángulo utilizando la fórmula dada
    area = base * altura
    # Mostramos el área del rectángulo por pantalla
    print("El área del rectángulo es:", area)

# Pedimos al usuario que ingrese la base y la altura del rectángulo
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Llamamos a la función
areaRectangulo (base, altura)

# Solución por Daniele Emiliano.