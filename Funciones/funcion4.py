# Calculando a los primeros numeros pares
print("Los numeros pares en los primeros 100 numeros")

def primero_pares(tope):
    # for en i, desde 0 hasta tope-1
    for i in range(0, tope):

        if (i % 2 == 0):
            print(i, end = " ")

primero_pares(100)
