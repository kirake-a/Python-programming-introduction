"""System module."""
# Listas

# Forma en la que declaramos una lista tipo cadena
# Los elementos de una lista se separan mediante comas
lista = ["Lunes", "Martes", "Miercoles", "Jueves", "viernes"]

# Asi es como se imprimen a los elementos de la lista
print(lista)

# Asi mostramos un elemento en especifico dado en la lista declarada
# Python tiene como indice para los arreglo a i = 0, hasta i = i-1
print(lista[0]) # Imprime al elemento cuyo indice sea 0

# Asi es como se imprime un cantidad de valores en la lista determinados
# Aqui se coloca al indice +1 de al que quiero llegar 
print(lista[0:3])

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.

numbers[0] = 111
print("\nPrevio contenido de la lista:", numbers)  # Imprimiendo contenido de la lista anterior.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

del numbers[1] # Elimina un elemento de la lista en la posicion [i]
print("Lista actuaizada con la eliminacion: ", numbers)
print("Longitud de la lista despues de la eliminacion: ", len(numbers))
