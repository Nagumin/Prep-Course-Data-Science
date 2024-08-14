# Escribe un programa que imprima los primeros 'n' números de la secuencia de Fibonacci

# Número de términos de la secuencia de Fibonacci a imprimir
n = int(input("Escriba una cantidad de números: "))

# Primeros dos números de la secuencia
a, b = 0, 1

# Imprimir los primeros n números de la secuencia
for numeros in range(n):
    print(a)
    a, b = b, a + b