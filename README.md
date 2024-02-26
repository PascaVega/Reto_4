# Reto_4
<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 4 - Parte 1</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Dado un número entero, determinar si ese número corresponde al código ASCII de una vocal minúscula.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Considerando las vocales ASCII ('a': 97 - 'e': 101 - 'i': 105 - 'o': 111 - 'u': 117), se crean condiciones para determinar si el carácter ingresado pertenece o no a la lista de datos (vocales).</td>
  </tr>
</table>

**Parte 1** 
```python
#RETO 4 - Parte 1
#Dado un número entero, determinar si ese número corresponde al código ASCII de una vocal minúscula.
#'a': 97 - 'e': 101 - 'i': 105 - 'o': 111 - 'u': 117

def introducir():
    numero = int(input("Ingrese un número para verificar si corresponde al código ASCII (digitos): "))
    verificar(numero)
    return

def verificar(numero):
    datos = {97,101,105,111,117}
    if numero in datos:
        print(f"El número {numero}, SÍ corresponde a una vocal minuscula del código ASCII")
        
    else:
        print(f"El número {numero}, NO corresponde a una vocal minuscula del código ASCII")
        
def continuar():
    opcion = int(input("¿Desea continuar verificando números? Marque 1 (sí) o 2 (no): "))
    return opcion

print("Programa para determinar si un número entero corresponde al código ASCII de una vocal minúscula")

while True:
    introducir()
    opcion = continuar()
    if opcion == 2:
        break  

# ! /\|=\/
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 4 - Parte 2</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Dada una cadena de longitud 1, determine si el código ASCII de primera letra de la cadena es par o no.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se incorpora la función <i>ord()</i> para obtener el número ordinal que está asociado con el caracter especificado. Con ayuda de esta función se obtiene el código del carácter y se crean condiciones para determiar si el número es par o impar.</td>
  </tr>
</table>

**Parte 2**
```python
#RETO 4 - Parte 2
#Dada una cadena de longitud 1, determine si el código ASCII de primera letra de la cadena es par o no.
 
def introducir():
    palabra = input("Ingrese una palabra: ")
    determinar(palabra)
    return

def determinar(palabra):
    letra = palabra[0]
    codigo = ord(letra)
    if codigo % 2 == 0:
        print("La primera letra de la cadena es PAR")
    else:
        print("La primera letra de la cadena es IMPAR")

def continuar():
    opcion = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

print("Programa para determinar si la primera letra de la cadena es par o no en el código ASCII.")

while True:
    introducir()
    opcion = continuar()
    if opcion == 2:
        break  

# ! /\|=\/
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 4 - Parte 3</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Dado un carácter, construya un programa en Python para determinar si el caracter es un dígito o no.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se incorpora la función <i>ord()</i> para obtener el número ordinal que está asociado con el caracter especificado, en caso de no estar asociado a ningún número o obtener un código más allá de 128 (código de 7 bits), este no pertenecera al código ASCII.</td>
  </tr>
</table>

**Parte 3**
```python
#RETO 4 - Parte 3
#Dado un carácter, construya un programa en Python para determinar si el caracter es un dígito o no.

def introducir():
    caracter = input("Ingrese un caracter: ")
    determinar(caracter)
    return

def determinar(caracter):
    num_caracter = ord(caracter)
    if 128 > num_caracter:
        print(f"El caracter {caracter} está en la ISCII")
    else:
        print(f"El caracter {caracter} no está en la ISCII")
    

def continuar():
    opcion = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

print("Programa para determinar si un caracter es un digito o no")

while True:
    introducir()
    opcion = continuar()
    if opcion == 2:
        break  

# ! /\|=\/
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 4 - Parte 4</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Dado un número real x, construya un programa que permita determinar si el número es positivo, negativo o cero. Para cada caso de debe imprimir el texto que se especifica a continuación:
        <li>Positivo: "El número x es positivo"</li>
        <li>Negativo: "El número x es negativo"</li>
        <li>Cero (0): "El número x es el neutro para la suma"</li>
    </td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se crean condiciones en donde el <i>número</i> ingresado se compara con 0 (mayor, menor o igual)</td>
  </tr>
</table>

**Parte 4**
```python
#RETO 4 - Parte 4
#Dado un número real x, construya un programa que permita determinar si el número es positivo, negativo o cero.

def introducir():
    numero = float(input("Ingrese un número (digitos): "))
    determinar(numero)
    return

def determinar(numero):
    if numero == 0:
        print(f"El número {numero} es el neutro para la suma.")
    elif numero > 0:
        print(f"El numero {numero} es positivo.")
    elif numero < 0:
        print(f"El numero {numero} es negativo.")
    else:
        print(f"El {numero} es invalido")
        introducir()

def continuar():
    opcion = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

print("Programa para determinar si un número es PAR o IMPAR")

while True:
    introducir()
    opcion = continuar ()
    if opcion == 2:
        break

# ! /\|=\/
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 4 - Parte 5</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Dado el centro y el radio de un círculo, determinar si un punto de R2 pertenece o no al interior del círculo.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se crean condiciones en donde el <i>número</i> ingresado se compara con 0 (mayor, menor o igual)</td>
  </tr>
</table>

**Parte 5** 
```python
#RETO 4 - Parte 5
#Dado el centro y el radio de un círculo, determinar si un punto de R2 pertenece o no al interior del círculo.
import math

def introducir():
    centro = input("Introduzca las coordenadas del centro del círculo. Ejemplo: 2,2 : ")
    radio = float(input("Introduzca el radio del cícurlo. Ejemplo: 2 : "))
    punto = input("Introduzca las coordenadas del punto. Ejemplo: 2,2 : ")
    determinar(centro, radio, punto)
    return
    

def determinar(centro, radio, punto):
    centro_X , centro_Y = map(float, centro.split(","))
    punto_X , punto_Y = map(float, punto.split(","))
    distancia = math.sqrt(((centro_X - punto_X)**2) + ((centro_Y - punto_Y)**2))
    if distancia <= radio:
        print(f"El punto {punto} sí está dentro del círculo")
    else:
        print(f"El punto {punto} no está dentro del círculo")

def continuar():
    opcion = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

print("Programa para determinar si un punto está dentro del área de un círculo")

while True:
    introducir()
    opcion = continuar()
    if opcion == 2:
        break

# ! /\|=\/
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 4 - Parte 5</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triángulo.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se crean condiciones en donde el <i>número</i> ingresado se compara con 0 (mayor, menor o igual)</td>
  </tr>
</table>

**Parte 6** 
```python
#RETO 4 - Parte 6
#Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triángulo.

def introducir():
    distancia_1 = float(input("Introduzca la primera distancia (digitos): "))
    distancia_2 = float(input("Introduzca la segunda distancia (digitos): "))
    distancia_3 = float(input("Introduzca la tercera distancia (digitos): "))
    determinar(distancia_1, distancia_2, distancia_3)
    return

def determinar(distancia_1, distancia_2, distancia_3):
    mayor = max(distancia_1, distancia_2, distancia_3)
    menor = min(distancia_1, distancia_2, distancia_3)
    if distancia_1 != mayor and distancia_1 != menor:
        medio = distancia_1
    elif distancia_2 != mayor and distancia_2 != menor:
        medio = distancia_2
    else:
        medio = distancia_3


    if menor + medio > mayor:
        print(f"SÍ es posible contruir un triangulo de medidas {distancia_1, distancia_2, distancia_3}")
    else:
        print(f"NO es posible contruir un triangulo de medidas {distancia_1, distancia_2, distancia_3}")

def continuar():
    opcion = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

print("Programa para determinar si es posible la construcción de un triángulo a partir de las medidas de los lados.")

while True:
    introducir()
    opcion = continuar()
    if opcion == 2:
        break

# ! /\|=\/
```
<h2>Bibliografía</h2>
    <div class="bibliografia">
        <table>
            <tr>
                <th>Referencia</th>
            </tr>
            <tr>
                <td>Código ASCII. (s. f.). El código ASCII. Recuperado el 26 de febrero de 2024, de https://elcodigoascii.com.ar/<a href="https://elcodigoascii.com.ar/"></a></td>
            </tr>
            <tr>
                <td>Recursos Python. (s. f.). Cómo obtener el código ASCII de un carácter y viceversa. Recuperado el 26 de febrero de 2024, de https://micro.recursospython.com/recursos/como-obtener-el-codigo-ascii-de-un-caracter.html <a href="https://micro.recursospython.com/recursos/como-obtener-el-codigo-ascii-de-un-caracter.html"></a></td>
            </tr> 
        </table>
    </div>
