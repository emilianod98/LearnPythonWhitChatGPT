'''
21. SUMA DE LOS DIVISORES DE UN NÚMERO

Escribir un programa que pida al usuario un número y muestre en pantalla la suma de sus divisores (excluyendo el propio número).
'''

# El usuario ingresa un numero
numero = int(input("Ingrese un número: "))

# Se crea una variable donde se van a almacenar los divesores del número
divisores = []

# Iteramos desde el 1 hasta el valor del numero...
for i in range(1, numero):
    # Si este es divisor del mismo, se almacena en la lista de divisores
    if numero % i == 0:
        divisores.append(i)

# Se suman todos los divisores 
suma_divisores = sum(divisores)

# Imprimimos por pantalla el numero y el resultado de la suma anterior
print("La suma de los divisores de", numero, "es", suma_divisores)


# Solución por ChatGPT