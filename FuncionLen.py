'''
La funcion len() nos permite identificar el numero de caracteres que posee un string, 
retorna longitud
'''

from gettext import find


nombre = "Nora"

len(nombre)

'''
Se puede ver mejor su funcionamiento en el IDLE de python, que ya viene
preinstalado
'''

# Esta accion nos permite hacer que la primera letra de una cadena sea mayusculo
palabra = 'ruben'

print(palabra.capitalize())

# Otros metodos importantes para el trabajo con cadenas de caracteres
'''
1. find # Encontrar caracteres o cadenas dentro de otras
2. index # ''
3. isalnum # Los que inician con 'is' se piensa que retorna un VERDADERO o BOOLEANO
4. isalpha
5. isdecimal
6. isdigit
7. islower
8. isupper
9. lower # Una copia con la cadena de caracteres en minuscula
10. upper # Una copia de la cadena de caracteres en mayuscula
'''