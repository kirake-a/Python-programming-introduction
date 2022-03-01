# condicionales, verificar si un numero es positivo, negativo o es el 0

numero = int(input("Digite un numero: "))

if numero > 0:
    print("Este valor es uno positivo.")
elif numero < 0:
    print("Este valor es uno negativo")
else:
    print("Este es el numero 0")