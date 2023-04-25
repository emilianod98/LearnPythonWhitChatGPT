'''
16. PRODUCTO DE LOS PRIMEROS `n` NÚMEROS

Escribir un programa que pida al usuario un número n y muestre en pantalla el producto de los primeros n números enteros positivos. Por ejemplo, si el usuario ingresa 4, el programa debe calcular 1 * 2 * 3 * 4 = 24.
'''

# Creo una función de productodelosAnteriores
def productodelosAnteriores (numero):
    # Verificar que el número sea positivo
    if numero < 0:
        print("El número ingresado no es positivo.")
    else:
        # Inicializar el producto como 1
        producto = 1
        # Calcular el producto de los primeros n números enteros positivos
        for i in range(1, numero + 1):
            producto *= i
        # Mostrar el resultado
        print("El producto de los primeros", numero, "números enteros positivos es:", producto)

# Pedimos al usuario que ingrese un número.
numero = int(input("Ingresa un número entero positivo: "))
        
# Llamamos a la función
productodelosAnteriores(numero)


# Solución por Daniele Emiliano.