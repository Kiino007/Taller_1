#Verificación de número primo:
# Usa un ciclo for para verificar si un número es divisible por algún número entre 2 y su raíz cuadrada.
# Si no tiene divisores, es primo.

numero = int(input("Ingrese el numero a verificar: "))

if numero < 2:
    print(f"{numero} no es numero primo")

else:
    raizc = numero ** 0.5
    print(f"La raíz cuadrada de {numero} es {raizc:.2f}")

    divisor = False

    rango = int(raizc) + 1
    for i in range(2, rango):
        if numero % i == 0:  
            divisor = True
            print(f"{numero} es divisible por {i}, por lo tanto es numero par.")
            break
    if not divisor:
        print(f"{numero} por lo tanto es número primo.")


    


        

    
    
    
