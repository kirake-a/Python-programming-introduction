"""system module."""

num1 = int(input("Ingresa primer numero: "))
num2 = int(input("Ingresa segundo numero: "))

sum = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2

mensaje = f"""Para los numeros {num1} y {num2}
el resultado de la suma es {sum}
el resultado de la suma es {resta}
el resultado de la suma es {mult}
el resultado de la suma es {div}
"""

print(mensaje)
