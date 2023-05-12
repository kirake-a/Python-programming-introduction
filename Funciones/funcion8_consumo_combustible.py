# El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. 
# Por ejemplo, en Europa, se muestra como la cantidad de combustible consumido por cada 100 kilómetros.
# En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.
# Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (millas por galón), y viceversa.
# Aquí hay información para ayudarte:
#    1 milla = 1609.344 metros.
#    1 galón = 3.785411784 litros 

def liters_100km_to_miles_gallon(liters):
    miles_in_100km = 100 / 1.609344
    total_gallons = liters / 3.785411784
    return (miles_in_100km / total_gallons)

def miles_gallon_to_liters_100km(miles):
    km_in_miles = (miles * 1609.344) / 100000
    liters = 3.785411784
    return (liters / km_in_miles)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
