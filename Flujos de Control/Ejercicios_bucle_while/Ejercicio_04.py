# Pedir al usuario un número y calcular su factorial.

numero = int(input("Ingrese el número al cual desea calcular el factorial: "))


if numero < 0:
    print("El número no puede ser negativo")
else:

    factorial = 1
    contador = 1

    while contador <= numero:
        factorial *= contador
        contador += 1

    print("El factorial de",numero,"es:",factorial)