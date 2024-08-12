# Escribe un programa que pida una nota y muestre la calificación en letras (A, B, C, D, F).

nota=input("Ingrese una nota de 0 a 5: ")

nota=float(nota)

if nota >= 0 and nota <= 0.9:
    print("Su calificación es F")
elif nota >= 1 and nota <= 1.9:
    print("Su calificación es D")
elif nota >= 2 and nota <= 2.9:
    print("Su calificación es C")
elif nota >= 3 and nota <= 3.9:
    print("Su calificación es B")
elif nota >= 4 and nota <= 5:
    print("Su calificación es A")
else:
    print("El número ingresado no se encuentra dentro del rango de notas permitido.")
    