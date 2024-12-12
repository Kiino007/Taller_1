#  Cantidad de vocales en una cadena: Recorre cada carácter de una cadena 
# de texto con un ciclo for y cuenta cuántos de ellos son vocales. 

texto = str(input("Digite el texto a ingresar"))
contador = 0
vocales = "aeiouAEIOU"

for caracter in texto:
    if caracter in vocales:
        contador += 1

print(f"El numero de vocales del texto es de: {contador}")