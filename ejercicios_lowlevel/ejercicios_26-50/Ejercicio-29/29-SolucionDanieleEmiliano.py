'''
29. COMPROBACIÓN DE SI UNA LISTA DE NÚMEROS ESTÁ ORDENADA

Escribe un programa que compruebe si una lista de números ingresada por el usuario está ordenada de manera ascendente o descendente.
'''

# Creamos una función llamada comprobarOrden
def comprobarOrden(lista):
    # Creamos dos variables que nos permitirán saber si se cumple cierta condición.
    ordenAscendente = True
    ordenDescendente = True
    # Iteramos dentro de la lista.
    for i in range(len(lista) - 1):
        # Si el indice situado es mayor al que le sigue.
        if lista[i] > lista[i+1]:
            # Mi lista esta ordenada de forma descendente, en caso de completar toda la iteracion y que no haya ningun problema.
            ordenAscendente = False
        # Si el indice situado es menor al que le sigue.
        elif lista[i] < lista[i+1]:
            # Mi lista esta ordenada de forma ascendente, en caso de completar toda la iteracion y que no haya ningun problema.
            ordenDescendente = False

    # Comprobamos el resultado
    if ordenAscendente:
        return print('La lista está ordenada de manera ascendente.')
    elif ordenDescendente:
        return print('La lista está ordenada de manera descendente.') 
    else:
        return print("La lista no está ordenada.")


# Se pide al usuario que ingrese una lista de números separados por comas.
numeros = input("Ingrese una lista de números separados por comas: ")

# Convertimos la cadena de entrada en una lista de números enteros.
lista = [int(numero) for numero in numeros.split(",")]

# Llamamos a la función
comprobarOrden(lista)


# Solución por Daniele Emiliano.