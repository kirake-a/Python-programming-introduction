'''
Repite la ejecucion del bloque de codigo mientras la expresion logica 
"Condicion" sea cierta
Es posible interrumpirla en cualquier momento con la instruccion BREAK'''

# Pregunta al usuario por un numero hasta que introduce 0

num = None

while num != 0:
    num = int(input("Introduce un numero: "))

    print(num)

'''while True:
    num = int(input("Digite un numero: "))

    print(num)

    if num == 0:
        break
'''

# Ambas sentencias while hacen exactamente lo mismo, pero con formas 
# distintas de ser escritas, y siendo que en algun caso una pueda ser 
# mas viable a ser utilizada que la otra y viceversa

