'''
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el 
nombre del usuario tantas veces como el número introducido.'''

def ciclo_imprime(i, num, nombre):

    while i <= num:
        print(nombre)

        i += 1

nombre = input("Digite su nombre: ")
num = int(input("Inserte un numero: "))

i = 1

ciclo_imprime(i, num, nombre)
