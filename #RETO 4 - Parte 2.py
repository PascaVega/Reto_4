#RETO 4 - Parte 2
#Dada una cadena de longitud 1, determine si el código ASCII de primera letra de la cadena es par o no.
 
def introducir():
    palabra : str = input("Ingrese una palabra: ")
    determinar(palabra)
    return

def determinar(palabra):
    letra : str = palabra[0]
    codigo : int = ord(letra)
    if codigo % 2 == 0:
        print("La primera letra de la cadena es PAR")
    else:
        print("La primera letra de la cadena es IMPAR")

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para determinar si la primera letra de la cadena es par o no en el código ASCII.")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/
