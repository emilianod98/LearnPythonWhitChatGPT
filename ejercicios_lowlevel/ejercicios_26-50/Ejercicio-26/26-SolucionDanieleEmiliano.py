'''
26. CÁLCULO DE LA MEDIANA DE UNA LISTA DE NÚMEROS

Escribe un programa que calcule y devuelva la mediana de una lista de números ingresada por el usuario.
'''

# Creamos la función calcularMediana
def calcularMediana(lista):
    # Odermaos la lista recibida
    listaOrdenada = sorted(lista)
    # Tomamos la longitud de la lista
    listaLongitud = len(listaOrdenada)
    # Si la lista tiene un número par de elementos
    if listaLongitud % 2 == 0:
        indiceMedioSuperior = listaLongitud // 2
        indiceMedioInferior = indiceMedioSuperior - 1
        mediana = (listaOrdenada[indiceMedioSuperior] + listaOrdenada[indiceMedioInferior]) / 2
    # O si la lista tiene un número impar de elementos 
    else:
        indiceMedio = listaLongitud // 2
        mediana = listaOrdenada[indiceMedio]
    # pedimos que nos devuelva una impresión de pantalla con la mediana.
    return print('La mediana de la lista es:', mediana)

# Solicitamos al usuario que ingrese una lista de números.
numeros = input("Ingrese una lista de números separados por comas: ")
# Convertimos todos los numeros en flotante y los almacenamos en una lista, tomando como referencia "," como separador de los números.
lista = [float(num) for num in numeros.split(",")]

# Llamamos a la función creada.
calcularMediana(lista)


# Solución por Daniele Emiliano.