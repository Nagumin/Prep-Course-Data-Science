"""Crear un programa que pida al usuario números
hasta que ingrese 0 y luego muestre la suma de todos
los números ingresados."""

#Pedir el número
numero = int(input("Ingrese un número: "))

#inicializar variable de suma en 0
suma = 0

#Mientras que el número no sea 0
while numero != 0:
    #Sumele el número ingresado a la suma y almacénelo en la misma suma
    suma += numero
    #Pedirel número otra vez
    numero = int(input("Ingrese un número: "))

print(suma)