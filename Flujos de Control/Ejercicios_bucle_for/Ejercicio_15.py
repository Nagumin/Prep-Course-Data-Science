#Encuentra el número mínimo en una lista de números

numin = float('inf') #Usamos infinito positivo para asegurar que cualquier número en la lista sea menor

lista = [98,101,23,44,200]

for i in lista:
    if i < numin:
        numin = i # Actualiza el mínimo si el número actual es menor
        
print(numin) # Imprime el número minimo