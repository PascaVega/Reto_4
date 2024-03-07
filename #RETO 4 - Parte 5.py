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