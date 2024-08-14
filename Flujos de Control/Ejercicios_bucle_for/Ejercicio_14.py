# Encuentra el número máximo en una lista de números

numax = 0

lista = [15,20,36,30,5,8,35,37]

for numero in lista:
    if numero > numax:
        numax = numero
print("El número máximo en esta lista es:",numax)