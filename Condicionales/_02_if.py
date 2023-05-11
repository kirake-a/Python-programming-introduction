"""system module."""

EDAD = 17

def _permido_entrada(edad):
    if edad > 54:
        print("Puede ver la pelicula con descuento")
    elif edad > 17:
        print("Puede ver la pelicula")
    else:
        print("No puede entrar")
        print("Ve a otro lado")

_permido_entrada(EDAD)
print()
_permido_entrada(55)
print()
_permido_entrada(16)

print("Listo")
