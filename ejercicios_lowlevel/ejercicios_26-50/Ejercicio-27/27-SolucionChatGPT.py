'''
27. CÁLCULO DE LA MODA DE UNA LISTA DE NÚMEROS

Escribe un programa que calcule y devuelva la moda de una lista de números ingresada por el usuario.
'''

# Se pide al usuario que ingrese una lista de números separados por comas.
numeros = input("Ingrese una lista de números separados por comas: ")

# Convertimos la cadena de entrada en una lista de números enteros.
lista_numeros = [int(numero) for numero in numeros.split(",")]

# Creamos un diccionario para contar la cantidad de veces que aparece cada número.
contador_numeros = {}
for numero in lista_numeros:
    if numero in contador_numeros:
        contador_numeros[numero] += 1
    else:
        contador_numeros[numero] = 1

# Encontramos el número con la mayor cantidad de apariciones.
mayor_apariciones = max(contador_numeros.values())

# Creamos una lista con los números que aparecen esa cantidad de veces.
moda = [numero for numero, apariciones in contador_numeros.items() if apariciones == mayor_apariciones]

# Mostramos la moda al usuario.
if len(moda) == 1:
    print(f"La moda es {moda[0]}.")
else:
    print(f"La moda es {', '.join(str(numero) for numero in moda)}.")


# Solución por ChatGPT