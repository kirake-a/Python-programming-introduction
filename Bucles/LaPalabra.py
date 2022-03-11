la_palabra = input("Inserte una palabra: ")
su_edad = int(input("Digite su edad: "))
un_numero = int(input("Inserte un valor positivo: "))

for i in range(10):
    print(la_palabra)

print("\nUsted entonces ha cumplido las siguientes edades: ")
for i in range(su_edad):
    print(i+1)

for i in range(un_numero, -1, -1):
    print("\n", i, end = ', ')

for i in range(0, un_numero+1, 2):
    print("\n", i, end=", ")

for i in range(un_numero):
    for j in range(i+1):
        print("*", end=" ")
    print(" ")