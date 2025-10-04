#add = lambda a, b: a + b
#print(add(10,4))

# El cuadrado de cada numero
numero = range(100)
cuadrado_numeros = list(map(lambda x: x**2, numero))
print ("cuadrado:", cuadrado_numeros )

# Si cumplen una funcion con filter

even_numeros = list(filter(lambda x: x%2 == 0, numero))
print ("pares:", even_numeros)

# lambda para usar funciones
# map aplica una funcion a cada elemento
# Range el rango de numero que quiero aplica la condicion
# filer filtra cada elemento de la funcion con la condicion

# Nuevo tema Recursividad de Fibonanci - Factoriales


