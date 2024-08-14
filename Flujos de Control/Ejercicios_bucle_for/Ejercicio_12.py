# Calcula el producto de los elementos de una lista

#Lista de elementos
lista = [1,2,3,4,5]

#Inicializamos el producto en 1 (Elemento neutro de multiplicación)

producto_total = 1

#Recorremos la lista multiplicando cada número por el producto total
for numero in lista:
    producto_total *= numero

#Imprimimos el resultado final
print(producto_total)