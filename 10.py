# Cantidad de dígitos de un número: Usa un ciclo for para recorrer los
# caracteres de un número convertido a cadena de texto y cuenta cuántos tiene

numero = int(input("ingrese un numero entero: "))
numerot = str(numero)
contador = 0

for digitos in numerot:
    contador += 1

print(f"El numero {numero} tiene {contador} digitos")