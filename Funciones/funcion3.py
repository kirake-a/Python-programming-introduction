# Programa que contiene una funcion que tiene la suma de dos enteros 

def suma_de_enteros(num1, num2):

    sumatoria = num1 + num2

    return sumatoria

num1 = int(input("Digite el valor del primer numero: "))
num2 = int(input("Digite el valor del segundo numero: "))

result = suma_de_enteros(num1, num2)

print(f"El resultado de la suma es: {result}")