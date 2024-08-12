#Escribe un programa que pida dos números y muestre si son iguales o diferentes.

numero1=input("Ingresa un número: ")
numero2=input("Ingresa otro número: ")

numero1=float(numero1)
numero2=float(numero2)

if numero1 == numero2:
    print("Los números son iguales")
else:
    print("Los números son diferentes")