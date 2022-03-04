'''
Escribir un programa que pida al usuario que introduzca una fraase en la 
consola y una vocal en minuscula, y despues muestre por pantalla la misma
frase pero con la vocal introducida en mayuscula'''

frase = input("Digite una frase: ")
vocal = input("Inserte una vocal en minuscula: ")

print(frase.replace(vocal, vocal.upper()))