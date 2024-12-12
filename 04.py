#Suma de los dígitos de un número:
# Recorre cada dígito de un número (convirtiéndolo en una cadena de texto) y
# suma sus valores utilizando un ciclo for.

numeros = [1, 2, 3, 4]
suma = 0

for numero in numeros:
    suma += numero
print(f"La suma de los dígitos es: {suma}")
