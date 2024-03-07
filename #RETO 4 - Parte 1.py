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