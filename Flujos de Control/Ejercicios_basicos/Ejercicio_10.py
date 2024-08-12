# Escribe un programa que pida un número y muestre si es un número primo o no.

# Solicita al usuario que ingrese un número
num = int(input("Ingresa un número: "))

# Un número primo es mayor que 1
if num > 1:
    # Asumimos que el número es primo hasta encontrar un divisor
    es_primo = True
    
    # Verificamos si tiene divisores desde 2 hasta num-1
    for i in range(2, num):
        if num % i == 0:
            es_primo = False  # Si encontramos un divisor, no es primo
            break
    
    # Mostramos el resultado
    if es_primo:
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
else:
    print(f"{num} no es un número primo.")
