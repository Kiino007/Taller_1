#Suma de los primeros n números naturales:
#Calcula la suma de los números desde 1 hasta n utilizando un ciclo for.
#Itera sobre los números en el rango de 1 a n y acumula su suma.


suma = 1

for i in range (1, 11):
    
    print( i, "+", suma, end=" ")
    suma += i
    print("=", suma)