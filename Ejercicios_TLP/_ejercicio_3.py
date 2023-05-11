"""system module."""

def _iniciales_(array):
    new_list = ""
    for i, _n in enumerate(array):
        new_list += _get_letra(_n) + " "
    return new_list

def _get_letra(palabra):
    new_palabra = palabra[0]
    return new_palabra

def _iniciales_2_(array):
    new_list = ""
    for i in array:
        new_list += i[0] + " "
    new_list.strip()
    return new_list

ARRAY = ["Ruben", "Moni", "Jorge", "Basto", "Curri", "Curi"]
iniciales = _iniciales_(ARRAY)
INICIALES_2 = _iniciales_2_(ARRAY)
print(f"Estas son las iniciales: {iniciales}")
print(f"Las otras iniciales {INICIALES_2}")
