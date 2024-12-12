# Media de una lista de números:
# Recorre cada elemento de una lista con un ciclo for, acumula su suma y divide entre el número total de elementos para calcular la media.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0
cantidad = 0

for numero in lista:
    suma += numero
    cantidad += 1
media = suma / cantidad

print(f"La cantidad de numeros en la lista es de: {cantidad}")
print(f"La suma de los numero es: {suma}")
print(f"La media de la lista es: {media}")