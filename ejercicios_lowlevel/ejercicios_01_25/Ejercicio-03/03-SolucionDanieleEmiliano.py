'''
03. MULTIPLICACIÓN DE DOS NÚMEROS

Escribir un programa que pida al usuario que ingrese dos números y muestre en pantalla el resultado de la multiplicación de ambos.
'''

# Creamos la función de Suma
def multiplicacion(numero1, numero2):
    resultado = numero1 * numero2
    # Mostrar la suma en la pantalla
    print("La multiplicación de", numero1, "y", numero2, "es igual a", resultado)


# Pedir al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))


# Llamar a la función suma con los dos números como argumentos.
multiplicacion(numero1, numero2)


#Confirmar, que termino de ejecutarse.
print("Programa terminado.")


# Solución por Daniele Emiliano.