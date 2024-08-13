# Imprime la tabla de multiplicar del 5

resultado = 0
multiplicacion = 5

for numeros in range (1,11):
    resultado = multiplicacion*numeros
    print(multiplicacion, "x",numeros,"=",resultado)