'''
04. DIVISIÓN DE DOS NÚMEROS

Escribir un programa que pida al usuario que ingrese dos números y muestre en pantalla el resultado de la división del primero por el segundo. Si el segundo número es cero, el programa debe mostrar un mensaje de error.
'''

# Pedimos al usuario que ingrese los dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Verificamos que el segundo número no sea cero
if num2 == 0:
    print("Error: el segundo número no puede ser cero")
else:
    # Realizamos la división del primer número por el segundo
    resultado = num1 / num2
    
    # Mostramos el resultado por pantalla
    print("El resultado de la división es:", resultado)


# Solución por ChatGPT