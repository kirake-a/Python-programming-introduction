# Programa que intercambia el valor de dos variables

valorA = int(input("Digite un valor a la variable A: "))
valorB = int(input("Digite un valor a la variable B: "))

# El intercambio de los valores de las variables
valorA, valorB = valorB, valorA

print(f"\nLos valores ahora son los siguientes: \nA = {valorA}  \nB = {valorB}")