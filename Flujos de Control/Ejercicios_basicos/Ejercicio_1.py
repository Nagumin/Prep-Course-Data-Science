# Escribe un programa que pida un número y muestre si es positivo o negativo.

numero=input("\nDigite un número entero positivo o negativo y presione ""Enter""\n \n")
numero = float(numero)
if numero==0:
    print("El número ingresado es 0")
elif numero>0:
    print("El número ingresado es positivo")
else:
    print("El número ingresado es negativo")