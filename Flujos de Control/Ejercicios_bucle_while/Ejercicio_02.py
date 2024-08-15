#Modificar el programa anterior para que imprima los números pares del 1 al 20.

contador = 0

while contador < 20:
    contador += 1
    if contador % 2 == 0:
        print(contador)