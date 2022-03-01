# Escribir una funcion que reciba un numero entero positivo y devuelva su factorial

#La funcion a continuacion recibe la entrada de datos del usuario
def leerValor():
   num = int(input("Digite el primer valor: "))

   return num

# Funcion para el calculo del factorial del numero dado mediante el uso de un ciclo FOR
def factorialDeUnNumero(valor):
    result = 1

    for i in range(valor):
        result *= i + 1
    
    return result

# Printeando el resultado final al usuario
def output(result, valor):
    print(f"\nEl resultado del factorial de {valor} es: {result}")


# Se inicia el programa
print("\nCalcular el factorial de un numero")

elNum = leerValor()

if elNum > 0:
    result_fact = factorialDeUnNumero(elNum)

    output(result_fact, elNum)
elif elNum < 0 or elNum == 0:
    print("Valor incorrecto, intente de nuevo...")
