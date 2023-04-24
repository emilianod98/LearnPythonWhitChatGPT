'''
04. DIVISIÓN DE DOS NÚMEROS

Escribir un programa que pida al usuario que ingrese dos números y muestre en pantalla el resultado de la división del primero por el segundo. Si el segundo número es cero, el programa debe mostrar un mensaje de error.
'''

# Creamos la función de Suma
def division(numero1, numero2):
    if numero2 == 0:
        print("Error: el segundo número no puede ser cero")
    else:
        resultado = numero1 / numero2
        # Mostrar la suma en la pantalla
        print("La divición de", numero1, "y", numero2, "es igual a", resultado)


# Pedir al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))


# Llamar a la función suma con los dos números como argumentos.
division(numero1, numero2)


#Confirmar, que termino de ejecutarse.
print("Programa terminado.")


# Solución por Daniele Emiliano.