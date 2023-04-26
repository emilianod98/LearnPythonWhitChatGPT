'''
15. SUMA DE LOS PRIMEROS `n` NÚMEROS

Escribir un programa que pida al usuario un número n y muestre en pantalla la suma de los primeros n números enteros positivos. Por ejemplo, si el usuario ingresa 5, el programa debe calcular 1 + 2 + 3 + 4 + 5 = 15.
'''

# Creamos una función llamada sumadelosAnteriores
def sumadelosAnteriores (numero):
    # Se inicializa la variable suma en cero.
    suma = 0
    # Se utiliza un ciclo for para recorrer todos los números enteros positivos desde 1 hasta n.
    for i in range(1, numero + 1):
        # En cada iteración del ciclo, se suma el valor de i a la variable suma.
        suma += i
    # Finalmente, se muestra en pantalla la suma total de los primeros n números enteros.
    print("La suma de los primeros", numero, "números enteros es:", suma)

# Primero, se le pide al usuario que ingrese un número entero positivo y se guarda en la variable n.
numero = int(input("Ingresa un número entero positivo: "))

# Se llama a la función
sumadelosAnteriores (numero)


# Solución por Daniele Emiliano.