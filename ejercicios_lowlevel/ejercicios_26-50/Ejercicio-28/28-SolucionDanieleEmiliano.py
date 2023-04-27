'''
28. CÁLCULO DEL RANGO DE UNA LISTA DE NÚMEROS

Escribe un programa que calcule y devuelva el rango de una lista de números ingresada por el usuario.
'''

# Creamos una función llamada listaRango
def listaRango (lista):
    # Creamos una variable que va a almacenar el valor minimo de la lista con la función min()
    minimo = min(lista)
    # Creamos una variable que va a almacenar el valor maximo de la lista con la función max()
    maximo = max(lista)
    # Y otra en donde se van a restar los valores maximo y minimo
    rango = maximo - minimo
    # Devolvemos en resultado en una impresión de pantalla
    print('El rango de la lista es: ', rango)

# Se pide al usuario que ingrese una lista de números separados por comas.
numeros = input("Ingrese una lista de números separados por comas: ")

# Convertimos la cadena de entrada en una lista de números enteros.
lista = [int(numero) for numero in numeros.split(",")]

# Llamamos a la función
listaRango(lista)


# Solución por Daniele Emiliano.