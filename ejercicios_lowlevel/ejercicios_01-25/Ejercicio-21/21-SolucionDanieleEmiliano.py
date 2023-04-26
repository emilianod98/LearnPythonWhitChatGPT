'''
21. SUMA DE LOS DIVISORES DE UN NÚMERO

Escribir un programa que pida al usuario un número y muestre en pantalla la suma de sus divisores (excluyendo el propio número).
'''

# Creo una función llamada sumadeDivisores.
def sumadeDivisores (numero):
    # Creamos una lista donde almacenaremos todos los divisores de ese número.
    divisores = []
    # Con un ciclo for, vamos a encontrar todos sus divisores y agregarlos a la lista creada.
    for div in range (1, numero):
        if numero % div == 0:
            divisores.append(div)
    # Realizamos la suma de los divisores.
    suma = sum(divisores)
    # Imprimimos por pantalla el resultado.
    print (f'La suma de los divisores del número: {numero}, es "{suma}"')


# El usuario ingresa un numero
numero = int(input("Ingrese un número: "))

# Llamamos a la función
sumadeDivisores(numero)


# Solución por Daniele Emiliano.