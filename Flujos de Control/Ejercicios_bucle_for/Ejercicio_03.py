# Imprime la suma de los números del 1 al 100

sumatotal = 0

for numeros in range (1,101):
    sumatotal+=numeros

#Print fuera del ciclo for, de lo contrario mostrará un resultado por cada iteración (suma)
print(sumatotal)