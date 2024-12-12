# Número más grande en una lista: Compara los números de una lista uno por
# uno utiliszando un ciclo for para encontrar el mayor de ellos.

num = [ 11, 23, 456, 65, 1, 54]

may = num[0]

for numero in num:
    if numero > may:
        may = numero

print(f"El numero mayor es: {may}")