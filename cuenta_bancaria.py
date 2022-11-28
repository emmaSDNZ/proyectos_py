class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellidos = apellido

class Cliente(Persona):
    
    def __init__(self, nombre, apellido, numeroCuenta, balance =0):
        super().__init__(nombre, apellido)
        self.numeroCuenta = numeroCuenta
        self.balance = balance

    def aumentaBalance(self, value):
        self.balance = self.balance + value
        print("Deposito aceptado")

    def restarBalance(self, value):
        if self.balance >= value:
            self.balance = self.balance - value
            print("Retido realizado")
        else:
            print("fondos insuficientes")

    def __str__(self):
        return f"""Cliente:
        Nombre: {self.nombre}, Apellido: {self.apellidos}
        Numero de cuenta: {self.numeroCuenta}
        Balance {self.balance}
        """

def crearCliente():
    nombre =str(input("Ingrese Nombre del cliente: "))
    apellido =str(input("Ingrese Apellido del cliente: "))
    numeroCuenta = int(input("Ingrese Numero de Cuenta del cliente: "))
    cliente = Cliente(nombre, apellido, numeroCuenta)

    return cliente

def incio():
    mi_cliente = crearCliente()
    print(mi_cliente)
    opcion = 0
    while opcion != "S":
        print("""  Selecciona un numero
        D - Deposito de dinero
        R- Extraccion de dinero
        S - Salir
        """)
        opcion = input()

        if opcion == "D":
            dinero = int(input("Ingresa deposito: "))
            mi_cliente.aumentaBalance(dinero)
        if opcion == "E":
            dinero = int(input("Retira deposito: "))
            mi_cliente.restarBalance(dinero)
        print(mi_cliente)

    print("Gracias por ser cliente")

incio()