'''
26. CÁLCULO DE LA MEDIANA DE UNA LISTA DE NÚMEROS

Escribe un programa que calcule y devuelva la mediana de una lista de números ingresada por el usuario.
'''

def mediana(lista):
    n = len(lista)
    lista_ordenada = sorted(lista)
    if n % 2 == 0:
        # Si la lista tiene un número par de elementos
        # la mediana es la media de los dos números del centro
        mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        # Si la lista tiene un número impar de elementos
        # la mediana es el número en el centro de la lista
        mediana = lista_ordenada[n // 2]
    return mediana

# Pedir al usuario que ingrese una lista de números separados por comas
numeros = input("Ingrese una lista de números separados por comas: ")
# Convertir la entrada en una lista de números
lista_numeros = [int(n) for n in numeros.split(',')]
# Calcular la mediana y mostrar el resultado
print("La mediana de la lista es:", mediana(lista_numeros))


# Solución por ChatGPT