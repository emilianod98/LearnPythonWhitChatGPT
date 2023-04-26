'''
02. RESTA DE DOS NÚMEROS

Escribir un programa que pida al usuario que ingrese dos números y muestre en pantalla la resta del segundo número al primero.
'''

# Creamos la función de resta
def resta(numero1, numero2):
    resultado = numero1 - numero2
    # Mostrar la resta en la pantalla
    print("La resta de", numero1, "y", numero2, "es igual a", resultado)


# Pedir al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))


# Llamar a la función resta con los dos números como argumentos.
resta(numero1, numero2)


#Confirmar, que termino de ejecutarse.
print("Programa terminado.")


# Solución por Daniele Emiliano.