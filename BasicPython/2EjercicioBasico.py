'''Determinar la solucion logica de la siguiente operacion:
((3+5x8)<3 and ((-6x4)/3+2<2)) or (a>b)'''

valorA = float(input("Digite un valor para la variable A: "))
valorB = float(input("Digite un valor para la variable B: "))

p = (3 + 5 * 8) < 3
q = ((-6 * 4) / 3 + 2) < 2
r = valorA > valorB

resultado = p and q or r

print(f"El resultado logico de la operacion es: {resultado}")