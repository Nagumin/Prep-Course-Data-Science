# Cuenta cuántos elementos en una lista son mayores que 10

contador = 0

lista = [5,12,7,15,3,20]

for i in lista:
    if i > 10:
        contador+=1 #Incrementa el contador por cada número mayor que 10
print(contador)