# Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4, y 5.

# Tu tarea es:

 # 1. escribir una línea de código que solicite al usuario que reemplace el número central en la lista
 #    con un número entero ingresado por el usuario (Paso 1)
 # 2. escribir una línea de código que elimine el último elemento de la lista (Paso 2)
 # 3. escribir una línea de código que imprima la longitud de la lista existente (Paso 3).

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

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
