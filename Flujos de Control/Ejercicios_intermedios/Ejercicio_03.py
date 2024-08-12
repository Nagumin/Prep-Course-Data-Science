#Imprimir los primeros 10 números de la serie Fibonacci

# Inicialización de las primeras variables
a, b = 0, 1
count = 0

# Número de elementos que queremos imprimir
n = 10

# Bucle para generar la serie Fibonacci
while count < n:
    print(a)
    a, b = b, a + b
    count += 1
