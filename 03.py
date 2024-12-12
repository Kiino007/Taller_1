#Números pares del 1 al 100:
# Usa un ciclo for para recorrer los números del 1 al 100 e imprime solo aquellos
# que sean divisibles entre 2 (números pares).

for i in range(1, 101):
    if i % 2 == 0:
      print(f"Numero par: {i}")
