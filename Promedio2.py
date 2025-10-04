class Estudiante():
   def __init__(self):
      self.name = str (input ("Ingresa nombre estudiante: "))
      self.age = int(input("Ingresa edad:"))


DatosE = Estudiante()
print (f"nombre estudiante:  {DatosE.name}")
print (f"Edad estudiante:  {DatosE.age}") 


def pedir_nota(numero):
    """Pide una nota válida entre 1 y 5"""
    while True:
        try:
            nota = float(input(f"Ingrese la nota {numero} (entre 1 y 5): "))
            if 1 <= nota <= 5:
                return nota
            else:
                print("⚠️ La nota debe estar entre 1 y 5. Intenta de nuevo.")
        except ValueError:
            print("⚠️ Entrada inválida. Debes ingresar un número.")

def main():
    print("=== Programa de Promedio de Notas ===")
    notas = []
    for i in range(1, 4):
        nota = pedir_nota(i)
        notas.append(nota)

    promedio = sum(notas) / len(notas)
    print(f"\n✅ Estudiante: {DatosE.name}, Edad: {DatosE.age}, El promedio de las notas es: {promedio:.2f}")

if __name__ == "__main__":
    main()

#def Info (self):
 #   print(f"nombre: {self.name}, edad: {self.age}, promedio: {self.promedio}")


      

      

            


