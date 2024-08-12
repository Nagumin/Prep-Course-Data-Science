# Crea un programa que pida un número y muestre si es par o impar.

#Pedimos el número por teclado
numero=input("\n Ingrese un número entero \n \n")
#convertimos el tipo de dato a int (entero)
numero=int(numero)

if numero % 2 == 0:
    print("\nEl número ingresado es par")
else:
    print("\nEl número ingresado es impar")