def leer_valores():
    num1 = float(input("Digite al valor 1: "))
    num2 = float(input("Digite al valor 2: "))

    return num1, num2

def funcion_suma(valor1, valor2):
    resul_sum = valor1 + valor2

    return resul_sum

def funcion_resta(valor1, valor2):
    result_rest = valor1 - valor2

    return result_rest

def funcion_mult(valor1, valor2):
    result_mult = valor1 * valor2

    return result_mult

def funcion_div(valor1, valor2):
    result_div = valor1 / valor2

    return result_div

def output(result, operacion):
    print(f"El resultado de la operacion ({operacion}) es: {result}")


# Aqui es donde inicia el programa, pidiendo la opcion deseada por el usuario...
print("Elija la operacion que desea realizar:")
print("1. Suma \n2. Resta \n3. Multiplicacion \n4. Dvision")

respuesta = int(input("Digite lo que desea realizar: "))

# Se evalua en if-elif-else la respuesta del usuario y se manda a funciones especializadas
if respuesta == 1:
    valor1, valor2= leer_valores()
    result = funcion_suma(valor1, valor2)

    operacion = 'suma'

    output(result, operacion)
elif respuesta == 2:
    valor1, valor2 = leer_valores()
    result = funcion_resta(valor1, valor2)

    operacion = 'resta'

    output(result, operacion)
elif respuesta == 3:
    valor1, valor2 = leer_valores()
    result = funcion_mult(valor1, valor2)

    operacion = 'multiplicacion'

    output(result, operacion)
elif respuesta == 4:
    valor1, valor2 = leer_valores()
    result = funcion_div(valor1, valor2)

    operacion = 'division'

    output(result, operacion)
else:
    print("Opcion no disponible por el momento.")