# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Verificar si el número es primo
if numero <= 1:
    print(f"{numero} no es un número primo.")
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")