"""system module."""

def _is_ordenado(array):
    counter = 0
    flag = False
    longitud = len(array)

    for i in range(0, longitud):
        print("im here")

        if (i+1 < longitud) and (array[i] < array[i+1]):
            counter += 1
    print(f"counter: {counter}")
    if counter == longitud-1:
        flag = True

    return flag

ARRAY = [60, 50, 40, 30, 20, 10, 5 , 4, 1]
print(_is_ordenado(ARRAY))
