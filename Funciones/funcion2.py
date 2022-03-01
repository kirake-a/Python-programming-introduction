def suma(a, b):
    result = a + b
    print(result)

    return result

def operaciones(a, b):
    suma = a + b
    multiplicacion = a * b
    resta = a - b

    return suma, multiplicacion, resta

sumaReturn, multiReturn, restaReturn = operaciones(5, 6)

resultado = suma(5, 6)

print(resultado)
print(sumaReturn, multiReturn, restaReturn)