'''
16. PRODUCTO DE LOS PRIMEROS `n` NÚMEROS

Escribir un programa que pida al usuario un número n y muestre en pantalla el producto de los primeros n números enteros positivos. Por ejemplo, si el usuario ingresa 4, el programa debe calcular 1 * 2 * 3 * 4 = 24.
'''

n = int(input("Ingresa un número entero positivo: "))

# Verificar que el número sea positivo
if n < 0:
    print("El número ingresado no es positivo.")
else:
    # Inicializar el producto como 1
    producto = 1
    
    # Calcular el producto de los primeros n números enteros positivos
    for i in range(1, n+1):
        producto *= i
        
    # Mostrar el resultado
    print("El producto de los primeros", n, "números enteros positivos es:", producto)


# Solución por ChatGPT