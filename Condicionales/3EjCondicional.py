# Hacer un programa que pida un caracter e indique si es una vocal o no

'''
El .lower() en la entrada de datos lo que hace es que cuando se digite
algun caracter lo transforme a un caracter minuscula, es por eso que si se
digitara un caracter vocal mayusculo, este siempre entraria y se marcaria como vocal,
porque seguiria entrando de menra satisfactoria en la estrucutra if-else
'''
letra = input("Digite un caracter: ").lower()

# letra = letra.lower()
'''
Con lo anterior lo que se hace es una copia a la variable letra, entonces
se hace una comparacion con letra.lower() y es cuando se le reasigna a la variable
letra el mismo caracter digitado previamente pero en minuscula
'''

if letra == 'a' or 'e' or 'i' or 'o' or 'u':
    print("La letra digitada es una vocal.")
else:
    print("La letra digitada no es una vocal.")
    