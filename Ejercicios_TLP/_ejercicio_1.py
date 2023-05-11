"""System module."""

def _segundos_tiempo(segundos, convertidor):

    if (convertidor == "s") | (convertidor == "S"):
        tiempo = segundos
        return tiempo

    if (convertidor == "m") | (convertidor == "M"):
        tiempo = segundos / 60
        return tiempo

    if (convertidor == "h") | (convertidor == "H"):
        tiempo = _segundos_tiempo(segundos, "m") / 60
        return tiempo

    if (convertidor == "d") | (convertidor == "D"):
        tiempo = _segundos_tiempo(segundos, "h") / 24
        return tiempo

    if (convertidor == "w") | (convertidor == "W"):
        tiempo = _segundos_tiempo(segundos, "d") / 7
        return tiempo

    if (convertidor == "mth") | (convertidor == "Mth"):
        tiempo = _segundos_tiempo(segundos, "w") / 4
        return tiempo

    if (convertidor == "y") | (convertidor == "Y"):
        tiempo = _segundos_tiempo(segundos, "mth") / 12
        return tiempo

_segundos = _segundos_tiempo(930, "s")
minutos = _segundos_tiempo(930, "m")
horas = _segundos_tiempo(930, "h")
dias = _segundos_tiempo(86400, "d")
semanas =_segundos_tiempo(604800, "w")
meses = _segundos_tiempo(2678400, "mth")
anios = _segundos_tiempo(32140800, "y")

print(str(_segundos) + " segundos")
print(str(minutos) + " minutos")
print(str(horas) + " horas")
print(str(dias) + " dias")
print(str(semanas) + " semanas")
print(str(meses) + " meses")
print(str(anios) + " años")
