# Hacer un programa que pida 2 numeros y se de cuenta cual de ello es par, 
# o si ambos lo son

valor1 = int(input("Digite al numero 1: "))
valor2 = int(input("Digite al numero 2: "))

siParV1 = valor1 % 2
siParV2 = valor2 % 2

if siParV1 == 0 and siParV2 == 0:
    print("Ambos valores son par")
elif siParV1 == 0:
    print("El primer numero es par")
elif siParV2 == 0:
    print("El segundo numero es par")
else:
    print("Ninguno de los valores es par")