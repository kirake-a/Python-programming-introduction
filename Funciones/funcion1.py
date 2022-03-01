'''Reglas generales de las funciones
1- No se ejecuta la funcion a menos que se le llame
2- la puede llamar la cantidad de veces que requiera
3- primero hay que definir la funcion, y despues llamarla
4- primero van los parametros requeridos y al final los opcionales
5- para cambiar el scope de una variable, utilizar return '''

# FUNCIONES SIN PARAMETROS

'''
def, es la reservada para definir funciones en python, ej: mifuncion():
'''

def derechos_humanos():
    print("Derecho a la vida")
    print("Derecho a la igualdad ante la ley")
    print("Derecho a la libertad")

derechos_humanos()

def derechos_mayorDeEdad():
    print("Derecho a votar")
    print("Derecho al trabajo")

# FUNCIONES CON PARAMETROS

'''
def mifuncion2(paramtro1, parametro2...)
    #conjunto de instrucciones
'''

def mayoria_de_edad(nombre, edad):
    print(f"Segun la edad de {nombre}, sus derechos son:")
    if edad >= 18:
        derechos_humanos()
        derechos_mayorDeEdad()
    else:
        derechos_humanos()


# FUNCIONES CON PARAMETROS OPCIONALES

'''
def mifuncion3(parametro1, parametro2 = valorpordefecto)
    #conjunto de instrucciones

    NOTA: los parametros opcionales siempre van a lo ultimo en la declaracion de la funcion
    Al decir que es un parametro opciones, a lo que se concluye, es que podemos mandarle ese valor
    a la funcion o no.
'''

def mayoria_de_edad2(edad, nombre = 'x'):
    print(f"Segun la edad de {nombre}, sus derechos son:")
      
    if edad >= 18:
        derechos_humanos()
        derechos_mayorDeEdad()
    else:
        derechos_humanos()

mayoria_de_edad2(19)

