'''
24. COMPROBACIÓN DE SI UNA CADENA DE TEXTO ES PALÍNDROMO

Escribir un programa que pida al usuario una cadena de texto y determine si es un palíndromo o no. Una cadena es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda. El programa debe mostrar en pantalla un mensaje indicando si la cadena es palíndromo o no.
'''

# Creamos la función palabraPalindromo
def palabraPalindromo (texto):
    # Convertimos el texto a minúsculas
    texto = texto.lower()
    # Creamos una variable para almacenar el texto invertido
    textoInvertido = ''
    for letra in range(len(texto)-1, -1, -1):
        textoInvertido += texto[letra]
    # Comparamos la cadena original con la invertida
    if texto == textoInvertido:
        print(f'La palabra "{texto}" es un palíndromo')
    else:
        print(f'La palabra "{texto}" no es un palíndromo')
    

# Pedimos al usuario que ingrese una cadena de texto
texto = input("Ingrese una cadena de texto: ")

# Llamamos a la función
palabraPalindromo (texto)


# Solución por Daniele Emiliano.