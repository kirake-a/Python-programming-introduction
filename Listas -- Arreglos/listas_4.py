# Esta es una lista existente de números ocultos en el sombrero.
hat_list = [1, 2, 3, 4, 5]

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
reemplazador = int(input("Ingresa el nuevo valor central de la lista: "))
MID = len(hat_list) / 2
hat_list[int(MID)] = reemplazador
print("Se ha cambiado el valor central de la lista: ", hat_list)

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]
print("Se ha eliminado correctamente el ultimo dato de la lista")

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Nueva longitud de la lista", len(hat_list))
print(hat_list)

hat_list.append(500)
print(hat_list)
hat_list.insert(3, 400)
print(hat_list)

for index, data in enumerate(hat_list):
    print("El valor ", data, " en la posicion ", index)

TOTAL = 0 # Se quiere calcular la suma de los valores almacenados dentro de la lista

for i in hat_list:
    TOTAL += i

print("El resultado total almacenado en la lista: ", TOTAL)
