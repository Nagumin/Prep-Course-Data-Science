# Crea un programa que pida un número y muestre "Aprobado" si es mayor o igual a 60, y "Reprobado" si es menor.

#Solicitar al usuario que ingrese un número por teclado
numero=input("Ingrese un número del 1 al 100: ")

#Se convierte el tipo de dato de la variable "numero" a int (entero)
numero=int(numero)

# Se valida para el caso de que el número esté fuera del rango solicitado, entonces muestre un mensaje de error:
if numero<1:
    print("El número ingresado no es válido por ser menor a 1")
elif numero>100:
    print("El número ingresado no es válido por ser mayor a 100")

#Se valida el propósito principal del programa <mostrar "Aprobado" si el número ingresado es mayor
# o igual a 60, y "Reprobado" si es menor.>
elif numero>=60:
    print("Aprobado")
else:
    print("Reprobado")