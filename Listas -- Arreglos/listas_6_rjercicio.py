"""system module."""

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

def list_without_repeating_element(list):
    """ Funcion que elimina los elemento repetidos de una lista"""

    lista_sin_repetidos = []

    for element in list:
        if element not in lista_sin_repetidos:
            lista_sin_repetidos.append(element)
    return lista_sin_repetidos

new_list = list_without_repeating_element(my_list)

print("La lista con elementos únicos: ", new_list)
