'''
05. CALCULADORA DE IMC

Escribir un programa que pida al usuario su peso en kilogramos y su altura en metros, y calcule su índice de masa corporal (IMC). El programa debe mostrar en pantalla el IMC y una clasificación según los siguientes criterios:

- IMC < 18.5: Bajo peso
- 18.5 <= IMC < 25: Peso normal
- 25 <= IMC < 30: Sobrepeso
- 30 <= IMC < 35: Obesidad grado 1
- 35 <= IMC < 40: Obesidad grado 2
- IMC >= 40: Obesidad grado 3
'''

# Creamos la función de CalculadoraIMC
def CalculadoraIMC(peso, altura):
    imc = peso / altura ** 2
    print("Su IMC es:", imc)

    # Clasificamos el IMC según los criterios dados
    if imc < 18.5:
        print("Bajo peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobrepeso")
    elif imc < 35:
        print("Obesidad grado 1")
    elif imc < 40:
        print("Obesidad grado 2")
    else:
        print("Obesidad grado 3")


# Pedir al usuario que ingrese dos números
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))


# Llamar a la función CalculadoraIMC con los dos números como argumentos.
CalculadoraIMC(peso, altura)


#Confirmar, que termino de ejecutarse.
print("Programa terminado.")


# Solución por Daniele Emiliano.