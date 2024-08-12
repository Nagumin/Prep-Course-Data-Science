# Solicitar al usuario un número y calcular la suma de todos los números naturales hasta ese número
# Solicitar un número al usuario
numero = int(input("Ingresa un número: "))

# Inicializar la variable que almacenará la suma
suma = 0

# Usar un bucle for para sumar todos los números naturales hasta el número ingresado
for i in range(1, numero + 1):
    suma += i

# Mostrar el resultado
print(f"La suma de todos los números naturales hasta {numero} es: {suma}")
