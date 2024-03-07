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