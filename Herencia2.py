# Ejercicio de Herencia
# Sonido de los animales 

class animales():
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        return "sonido del animal"

# Clase Hija

class Perro (animales):
    def sonido (self):
        return f"{self.nombre} dice: Gua Gua"

class Gato (animales):
        def sonido(self):
             return f"{self.nombre} dice: Miau Miau"
        
#Programa Principal
if __name__ == "__main__":
     perro = Perro ("Firulais")
     gato = Gato ("Michino")

     print (perro.sonido())
     print (gato.sonido())




