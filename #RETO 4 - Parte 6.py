#RETO 4 - Parte 6
#Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triángulo.

def introducir():
    distancia_1 : float = float(input("Introduzca la primera distancia (digitos): "))
    distancia_2 : float = float(input("Introduzca la segunda distancia (digitos): "))
    distancia_3 : float = float(input("Introduzca la tercera distancia (digitos): "))
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
    elif menor == medio == mayor:
        print(f"SÍ es posible contruir un triangulo de medidas {distancia_1, distancia_2, distancia_3}")
    else:
        print(f"NO es posible contruir un triangulo de medidas {distancia_1, distancia_2, distancia_3}")

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para determinar si es posible la construcción de un triángulo a partir de las medidas de los lados.")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/
