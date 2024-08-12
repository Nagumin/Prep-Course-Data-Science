#Crea un programa que pida un carácter y determine si es una vocal o una consonante.

vocales = "aeiouAEIOU"

letra = input("Ingrese una letra: ")

if letra in vocales:
    print("Es una vocal.")
else:
    print("Es una consonante.")