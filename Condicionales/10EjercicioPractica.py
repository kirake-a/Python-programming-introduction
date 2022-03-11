def tipo_pizza(tipo_pizza_var):

    if tipo_pizza_var == 1:
        pizza = "Vegetariana"
        print("Esta pizza puede contener: \n1- Pimiento \n2- Tofu")
        cual_pizza = int(input("El ingrediente que desea: "))

        ingrediente = el_ingrediente(cual_pizza)

    elif tipo_pizza_var == 2:
        pizza = "No vegetariana"
        print("Esta pizza puede contener: \n3- Peperoni \n4- Jamon \n5- Salmon")
        cual_pizza = int(input("El ingrediente que desea: "))

        ingrediente = el_ingrediente(cual_pizza)

    output(pizza, ingrediente)

def el_ingrediente(cual_pizza):

    if cual_pizza == 1:
        ingrediente = "Pimiento"
    elif cual_pizza == 2:
        ingrediente = "Tofu"
    elif cual_pizza == 3:
        ingrediente = "Peperoni"
    elif cual_pizza == 4:
        ingrediente = "Jamon"
    elif cual_pizza == 5:
        ingrediente = "Salmon"

    return ingrediente

def output(pizza, ingrediente):
    print("\nTipo de pizza: ", pizza)
    print("Ingrediente agregado: ", ingrediente)



print("Hoy tenemos pizzas")
print("1. Pizza vegetariana")
print("2. Pizza no vegetariana")
tipo_pizza_var = int(input("Digite el tipo de pizza que desea adquirir: "))

tipo_pizza(tipo_pizza_var)