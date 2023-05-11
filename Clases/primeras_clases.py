"""System module."""

class Employee:
    """Construccion de 'Employee'"""

    company = "Empresa Fantasma"

    def __init__(self):
        print("Hello World")
    
    def func_message(self):
        """Funcion de bienvenida de un nuevo trabajador"""

        print("Welcome to Programming Language")

trabajdor = Employee()

print(trabajdor.company)
print(trabajdor.func_message())
