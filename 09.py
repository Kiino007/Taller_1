# Máximo común divisor (MCD): Encuentra el MCD de dos números utilizando
# el algoritmo de Euclides con un ciclo while, que repite el cálculo del residuo
# hasta que uno de los números sea cero.

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

print("El MCD de", num1, "y", num2, "es:", end = " ")

while num2 != 0:
     num1, num2 = num2, num1 % num2

print(num1)