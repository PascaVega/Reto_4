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