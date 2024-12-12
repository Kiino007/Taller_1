# Suma de los dígitos de un número con ciclos: 
#Extrae cada dígito de un número utilizando operaciones matemáticas y acumula su suma dentro de un ciclo.

numero = int(input("Ingrese un numero entero: "))

suma = 0

while numero > 0:
    digito = numero % 10
    suma += digito
    numero //= 10 

print(f"La suma de los digitos es: {suma}")