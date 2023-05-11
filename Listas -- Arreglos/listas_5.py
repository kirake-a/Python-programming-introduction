list_1 = [1]
list_2 = list_1 # Aqui copia el nombre de la variable, no la lista en si
list_1[0] = 2
# Lo que hace es que ambas listas funcionan como una sola
# al cambiar los valores en la lista1 tambien se hara en lista2
print("Resultado obtenido con la lista1: ", list_1, ". Se nota la dependencia entre listas")
print("Resultado obtenido con la lista2: ", list_2, ". Se nota la dependencia entre listas")
print(list_2) 

list_1_aux = [1]
list_2_aux = list_1_aux[:] # Aqui si se copian los valores de ambas listas
# my_list[inicio:fin] copia de una seccion determinada de la lista
# la lista anterior contiene (fin - inicio) elementos, es decir, no incluye al elemento[fin]
list_1_aux[0] = 2
# Ahora con la modificacion ambas listas funcionan de manera independiente
print("Resultado obtenido con la lista1 auxiliar: ", list_1_aux)
print("Resultado obtenido con la lista2 auxiliar: ", list_2_aux)