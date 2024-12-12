#Factorial de un número dado:
# Encuentra el factorial de un número multiplicando todos los números desde 1 hasta
# ese número con un ciclo for. Asegúrate de inicializar la variable acumuladora en 1.

# Declaramos variables a usar en el ejercicio

factorial = 5
inicio = 1

# la variable factorial se puede reemplazar por un int input para pedirle el numero que desee el usuario
# la variable inicio marca el inicio en 1 que siempre va tener la operacion

for i in range(inicio, factorial):
    factorial *= i
    
    # En el ciclo for el numero de iteraciones representada por i es el que aumentara y se multiplicara por el valor que vaya obteniendo factorial 


    print(f"El resultado es {factorial}")
    
    # Imprimira el resultado del factorial
