'''
25. ORDENAMIENTO DE UNA LISTA DE NÚMEROS

Escribir un programa que pida al usuario que ingrese dos números y muestre en pantalla el resultado de la división del primero por el segundo. Si el segundo número es cero, el programa debe mostrar un mensaje de error.
'''

# Creamos una función llamada division
def division (numero1, numero2):
    # Comprobamos que el segundo valore sea distinto a "0"
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f'El resultado de la división de {numero1} y {numero2} es: {resultado}')
    else:
        print('El segundo valor ingresado no puede ser "0"')
    

# Pedimos al usuario que ingrese los dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Llamamos a la función creada
division (numero1, numero2)


# Solución por Daniele Emiliano.