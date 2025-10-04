# Ejercicio de Herencia
#  ventas de flores

class Ventas():
    def __init__ (self, Flores, precio):
        self.Flores = Flores
        self.precio = precio
        self.is_available= True

    def Venta_FLores(self):
        if self.is_available:
            self.is_available = False
            print (" no hay flores disponibles")
        else: print(" no hay flores")
                    
    def get_precio(self):
        return self.precio
        
    def check_available(self):
        return self.is_available
        
class inventario:
    def __init__ (self):
        self.inventario = []
    
    def add_flores (self, flores):
        self.inventario.append(flores)

Ventas1 = Ventas ("rosas", 0)
Ventas2 = Ventas ("margaritas", 90) 

Inventario1 = inventario()
Inventario1.add_flores(Ventas1)
Inventario1.add_flores(Ventas2)

for venta in Inventario1.inventario:
    print(f"Flor: {venta.Flores}, Precio: {venta.get_precio()}, Disponible: {venta.check_available()}") 

    Ventas1.Venta_FLores()
    print(f"Disponible después de venta: {Ventas1.check_available()}")
# ...existing code...

        