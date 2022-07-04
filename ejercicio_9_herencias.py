class Persona():

    def __init__(self, edad, nombre, telefono):

        self.__edad__ = edad
        self.__nombre__ = nombre
        self.__telefono__ = telefono

    def descripcion(self):

        print('La edad del cliente es: ', self.__edad__, '\nEl nombre del cliente es: ', self.__nombre__,
              '\nEl telefono del cliente es: ', self.__telefono__)

class Cliente(Persona):

    def credito(self, credito):

        self.credito = credito

    def descripcionCredito(self):

        print('El cliente tiene un credito de: ', self.credito, ' dolares')

    
class Trabajador(Persona):
    
    def salario(self, salario):

        self.salario = salario

    def descripcionSalario(self):

        print('El trabajador tiene un salario de: ', self.salario, ' dolares')

print('Información del cliente:')    

cliente1 = Cliente(27, 'Jose', 412988)
cliente1.descripcion()
cliente1.credito(2000)
cliente1.descripcionCredito()

print('Información del trabajador:')

trabajador1 = Trabajador(45, 'Maria', 4149995)
trabajador1.descripcion()
trabajador1.salario(5000)
trabajador1.descripcionSalario()