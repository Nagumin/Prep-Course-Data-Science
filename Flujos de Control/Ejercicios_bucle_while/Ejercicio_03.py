# Calcular la suma de los números del 1 al 100.

suma = 0
numero = 1

while numero <= 100:
    #Suma el valor actual de número a la variable suma.
    suma += numero
    #Incrementa el valor de número en 1 para pasar al siguiente número.
    numero += 1

print("La suma de los números del 1 al 10 es:",suma)