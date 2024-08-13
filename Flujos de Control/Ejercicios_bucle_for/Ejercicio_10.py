"""Imprime los números del 1 al 10, pero detente si
llegas al número 5"""

for numero in range (1,11):
    if numero == 6:
        break
    else:
        print(numero)