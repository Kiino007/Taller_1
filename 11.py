# Invertir un número: Recorre los dígitos de un número desde el principio hasta
# el final utilizando un ciclo for y constrúyelo en orden inverso

numero = int(input("Ingrese un numero entero: "))
numerotex = str(numero)
numeroinver = ""

for digito in numerotex[::-1]:
    numeroinver += digito

numeroinver = int(numeroinver)

print(f"El número invertido de {numero} es {numeroinver}.")