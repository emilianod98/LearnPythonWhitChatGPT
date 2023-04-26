'''
14. FACTORIAL DE UN NÚMERO

Escribir un programa que pida al usuario un número y muestre en pantalla su factorial, es decir, el producto de todos los números enteros positivos desde 1 hasta ese número. Por ejemplo, el factorial de 5 es 5 * 4 * 3 * 2 * 1 = 120.
'''

# Creamos la función factorial
def factorial (numero):
    # Inicializamos la variable factorial en 1
    var = 1
    # Iteramos desde 1 hasta el número ingresado por el usuario
    for i in range(1, numero + 1):
        var *= i
    # Mostramos el factorial por pantalla
    print("El factorial de", numero, "es", var)


# Pedimos al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Llamamos a la función
factorial (numero)


# Solución por Daniele Emiliano.