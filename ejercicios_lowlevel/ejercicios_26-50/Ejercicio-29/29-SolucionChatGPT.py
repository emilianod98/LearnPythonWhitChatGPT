'''
29. COMPROBACIÓN DE SI UNA LISTA DE NÚMEROS ESTÁ ORDENADA

Escribe un programa que compruebe si una lista de números ingresada por el usuario está ordenada de manera ascendente o descendente.
'''

def orden(lista):
    ascendente = sorted(lista)  # Ordenamos la lista de forma ascendente
    descendente = sorted(lista, reverse=True)  # Ordenamos la lista de forma descendente
    if lista == ascendente:  # Si la lista original es igual a la lista ordenada de forma ascendente
        print("La lista está ordenada de forma ascendente.")
    elif lista == descendente:  # Si la lista original es igual a la lista ordenada de forma descendente
        print("La lista está ordenada de forma descendente.")
    else:  # Si la lista no está ordenada de ninguna forma
        print("La lista no está ordenada.")


# Pedimos al usuario que ingrese los números separados por espacios
numeros = input("Ingrese los números separados por espacios: ")

# Convertimos los números a una lista de enteros
lista_numeros = [int(num) for num in numeros.split()]

orden(lista_numeros)


# Solución por ChatGPT