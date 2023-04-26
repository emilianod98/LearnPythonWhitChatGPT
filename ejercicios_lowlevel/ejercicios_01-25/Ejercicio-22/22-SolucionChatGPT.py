'''
22. INVERSIÓN DE UNA CADENA DE TEXTO

Escribir un programa que pida al usuario una cadena de texto y muestre en pantalla la cadena invertida, es decir, con los caracteres en orden inverso. Por ejemplo, si el usuario ingresa "hola", el programa debe mostrar "aloh".
'''

cadena = input("Ingrese una cadena de texto: ")
cadena_invertida = cadena[::-1]
print(cadena_invertida)

# En este código, se utiliza la técnica de "slicing" en Python para invertir la cadena. La sintaxis [::1] significa "desde el principio hasta el final, tomando cada carácter en pasos de -1".


# Solución por ChatGPT