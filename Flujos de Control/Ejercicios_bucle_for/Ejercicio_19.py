#Escribe un programa que cuente cuántas veces aparece un carácter en una cadena de texto

def contar_caracter(cadena, caracter):
    
    """Cuenta cuántas veces aparece un carácter en una cadena usando el count().

    Args:
        cadena: La cadena de texto donde buscar el carácter.
        caracter: El carácter a contar.add()
        
    Returns:
        El número de veces que aparece el carácter en la cadena."""
    
    # Se crea una variable llamada contador y se inicializa en 0
    # Esta variable se utilizará para llevar la cuenta de las veces
    # que se encuentra el carácter en la cadena.    
    contador = 0
    
    for letra in cadena:
        if letra == caracter:
            contador += 1
    return contador

# Ejemplo de uso:
texto = input("Escriba una palabra o una frase corta: ")
caracter_a_buscar = input("Escriba la letra o caracter que quiere buscar en \nsu palabra o frase: ")

resultado = contar_caracter(texto, caracter_a_buscar)
print(f"El caracter '{caracter_a_buscar}' aparece {resultado} veces en la cadena.")