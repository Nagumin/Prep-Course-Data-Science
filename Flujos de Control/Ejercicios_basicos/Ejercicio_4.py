#Escribe un programa que pida un número y muestre si es múltiplo de 5.

#Pedimos el número por teclado
numero=input("\n Ingrese un número entero \n \n")
#convertimos el tipo de dato a int (entero)
numero=int(numero)

if numero % 5 == 0:
    print("\nEl número ingresado es múltiplo de 5")
else:
    print("\nEl número ingresado no es múltiplo de 5")