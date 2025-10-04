# Crear la funcion
def add(a, b):
    return a+b
def restar (a, b):
    return a-b
def multiplicar (a, b):
    return a*b

def calculadora():
    while True: # sirve para continuar con el bucle
        print("seleccione una operacion")
        print("1. suma")
        print("2. resta")
        print("3. multiplicacion")
        print("4. salir")
        
        opcion = input("ingrese una opcion(1,2,3,4): ")
        if opcion == "4":
           print("se acabo  el juego")
           break
        if opcion in ["1","2","3"]:
            num1 = float(input("ingrese numero1: "))
            num2 = float(input("ingrese numero2: "))

            if opcion == "1":
                print(" la suma:", add(num1,num2))
            elif opcion == "2":
                print(" la resta:", restar(num1,num2))
            elif opcion == "3":
                print(" la multiplicaion:", multiplicar(num1,num2))
        else:
            print("opcion no vlida")            
           

calculadora()


