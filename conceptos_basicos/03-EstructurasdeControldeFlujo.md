<p align="center">
  <img src="../src/Learn-python.png">
</p>


# ***Estructuras de control de flujo***

Las estructuras de control de flujo son una parte fundamental de cualquier lenguaje de programación y permiten controlar el flujo de ejecución de un programa. En Python, las estructuras de control de flujo más comunes son las siguientes:


### **Estructuras Condicionales:** 

Las estructuras condicionales permiten ejecutar diferentes bloques de código dependiendo de si se cumple o no una condición. En Python, la estructura condicional más común es el `if`, que se utiliza de la siguiente manera:

```
if condicion:
    # Bloque de código que se ejecutará si se cumple la condición
else:
    # Bloque de código que se ejecutará si no se cumple la condición
```

Por ejemplo, aquí hay un código que muestra cómo utilizar una estructura condicional para determinar si un número es par o impar:

```
numero = 5

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
```


### **Estructuras de Bucles:** 
Las estructuras de bucles permiten ejecutar un bloque de código varias veces. En Python, las estructuras de bucles más comunes son el `while` y el `for`.


El `while` se utiliza para ejecutar un bloque de código mientras se cumpla una condición:

```
while condicion:
    # Bloque de código que se ejecutará mientras se cumpla la condición
```

Por ejemplo, aquí hay un código que utiliza un bucle `while` para contar hasta 5:

```
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```
<br>


El `for` se utiliza para recorrer una secuencia de elementos, como una lista o una cadena de texto:

```
for elemento in secuencia:
    # Bloque de código que se ejecutará para cada elemento de la secuencia
```

Por ejemplo, aquí hay un código que utiliza un bucle `for` para recorrer una lista de nombres e imprimir cada uno de ellos:

```
nombres = ["Juan", "Ana", "Pedro"]

for nombre in nombres:
    print(nombre)
```

Es importante comprender cómo funcionan las estructuras de control de flujo en Python, ya que te permiten controlar el flujo de ejecución de tu programa y hacer que sea más dinámico e interactivo. Con ellas, podrás crear programas más sofisticados y realizar operaciones más complejas.
