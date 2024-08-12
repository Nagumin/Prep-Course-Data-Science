# Escribe un programa que pida tres números y muestre el mayor de los tres.

numero1=input("Ingrese el primer número: ")
numero2=input("Ingrese el segundo número: ")
numero3=input("Ingrese el tercer número: ")

numero1=int(numero1)
numero2=int(numero2)
numero3=int(numero3)

if numero1>numero2 and numero1>numero3:
    print("El número mayor es el: ",numero1)
elif numero1<numero2 and numero2>numero3:
    print("El número mayor es el: ",numero2)
elif numero1<numero3 and numero3>numero2:
    print("El número mayor es el: ",numero3)
else:
    print("Los números son iguales.")