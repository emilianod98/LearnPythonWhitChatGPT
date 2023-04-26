'''
23. CÁLCULO DE LA LONGITUD DE UNA CADENA DE TEXTO

Escribir un programa que pida al usuario una cadena de texto y muestre en pantalla su longitud, es decir, el número de caracteres que tiene la cadena.
'''

# Creo una función llamada longitudTexto
def longitudTexto (texto):
    # Creamos un contador.
    contador = 0
    # Iteramos por cada letra del texto
    for letra in texto:
        # le decimos a nuestro contado se valla sumando 1.
        contador += 1
    # imprimimos por pantalla el resultado.
    print (f'La longitud del texto es de {contador} carácteres')


# Se pide al usuario que ingrese la cadena de texto mediante la función input().  
texto = input("Ingrese una cadena de texto: ")

# Llamamos a la función
longitudTexto (texto)


# Solución por Daniele Emiliano.