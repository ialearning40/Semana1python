class Carros:
 def __init__(self, tipo, age): #constructor es una funcion de las clases atributos tipo, año
       self.tipo = tipo
       self.age = age
 def type(self):
     print(f"el carro es {self.tipo} y es del año {self.age}")

carro1 = Carros("BMW", 2000)
carro2 = Carros("Audi", 1994)

carro1.type()
carro2.type()

### Metodo

class DaviviendaAcount:
    def __init__(self, cuenta, balance):
        self.cuenta = cuenta
        self.balance = balance
        self.is_active = True

    def deposito (self, valor):
       if self.is_active:
        self.balance += valor
        print(f"se ha depositado {valor}. saldo actual {self.balance}")
       else:
        print(f"cuenta inactiva")

    def retirar (self, valor):
        if self.is_active:
            if valor <= self.balance:
                self.balance -= valor
                print(f"se ha retirado {valor} saldo actual {self.balance}")

    def desactivarcuenta(self):
        self.is_active = False
        print("cuenta desactivada")

#crear el objeto
cuenta1 = DaviviendaAcount ("Ana", 500)
cuenta2 = DaviviendaAcount("Rosa", 1000)

#llamado al metodo
cuenta1.retirar(100)






