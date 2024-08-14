# Invierte una lista usando un ciclo for

invertida = []

lista = ["manzanas","peras","uvas","aguacates","fresas"]

for frutas in range(len(lista) - 1, -1, -1):
    invertida.append(lista[frutas])

print(invertida)