'''
22. INVERSIÓN DE UNA CADENA DE TEXTO

Escribir un programa que pida al usuario una cadena de texto y muestre en pantalla la cadena invertida, es decir, con los caracteres en orden inverso. Por ejemplo, si el usuario ingresa "hola", el programa debe mostrar "aloh".
'''

# Creamos la función cadenaInvertida
def cadenaInvertida(texto):
    # Creamos una variable para almacenar el texto invertido
    textoInvertido = ''
    for letra in range(len(texto)-1, -1, -1):
        textoInvertido += texto[letra]
    print(f'El texto escrito es: {texto} y su versión invertida es: "{textoInvertido}"')

# Pedimos al usuario que ingrese un texto
texto = input('Ingrese un texto: ')

# Llamamos a la función
cadenaInvertida(texto)


# Solución por Daniele Emiliano.