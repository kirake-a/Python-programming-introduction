# Elementos basicos de python

## Definiendo variables
variableA = float(input("Inserte el valor de la variable a: "))
variableB = float(input("\nDigite el valor de la variable b: "))
variableC = float(input("\nDigite el valor de la variable c: "))

# Operaciones algebraicas
numerador = (variableA ** 3) * ((variableB ** 2) - 2 * (variableA * variableC))

resultadoFinal = numerador / (2 * variableB)

# Output
print(f"\nEl resultado de la operacion por formula es: {resultadoFinal}")