'''
25. ORDENAMIENTO DE UNA LISTA DE NÚMEROS

Escribir un programa que pida al usuario que ingrese dos números y muestre en pantalla el resultado de la división del primero por el segundo. Si el segundo número es cero, el programa debe mostrar un mensaje de error.
'''

# Pedimos al usuario que ingrese los dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Verificamos si el segundo número es cero
if num2 == 0:
    print("Error: No se puede dividir entre cero.")
else:
    # Si el segundo número es distinto de cero, realizamos la división y mostramos el resultado
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)


# Solución por ChatGPT