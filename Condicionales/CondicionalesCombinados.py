# Condicionales combinados

edad = int(input("Digite su edad: "))


'''if edad > 18 and edad <= 100:
    print("Usted es mayor de edad")
elif edad > 0 and edad < 18:
    print("No es mayor de edad")
else:
    print("Esta edad es incorrecta")'''
# Lo anterior es una buena opcion para resolver el problema, 
# pero tambien se puede usar:

if 0 < edad < 100:
    print("Edad correcta")
    if edad > 18:
        print("Esta es un persona mayor de edad")
else:
    print("Edad incorrecta")
