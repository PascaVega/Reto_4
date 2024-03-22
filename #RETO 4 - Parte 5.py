#RETO 4 - Parte 5
#Dado el centro y el radio de un círculo, determinar si un punto de R2 pertenece o no al interior del círculo.
import math

def introducir():
    centro_X : float = float(input("Introduzca las coordenadas del centro del círculo en x. Ejemplo: 2 : "))
    centro_Y : float = float(input("Introduzca las coordenadas del centro del círculo en y. Ejemplo: 2 : "))
    radio : float = float(input("Introduzca el radio del cícurlo. Ejemplo: 2 : "))
    punto_X : float = float(input("Introduzca las coordenadas del punto en x. Ejemplo: 2 : "))
    punto_Y : float = float(input("Introduzca las coordenadas del punto en y. Ejemplo: 2 : "))
    determinar(centro_X, centro_Y, radio, punto_X, punto_Y)
    return
    

def determinar(centro_X, centro_Y, radio, punto_X, punto_Y):
    distancia = (((centro_X - punto_X)**2) + ((centro_Y - punto_Y)**2))**(1/2)
    punto = str(punto_X) + " , " + str(punto_Y)
    if distancia <= radio:
        print(f"El punto {punto} sí está dentro del círculo")
    else:
        print(f"El punto {punto} no está dentro del círculo")

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para determinar si un punto está dentro del área de un círculo")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/
