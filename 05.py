#Tabla de multiplicar de un número:
# Genera la tabla de multiplicar de un número dado del 1 al 10 utilizando un ciclo for.
# Por cada iteración, calcula el producto y muéstralo.

numero = 8

for multi in range(1, 11):
    resultado = numero*multi
    print(f"{numero} X {multi} = {resultado}")
