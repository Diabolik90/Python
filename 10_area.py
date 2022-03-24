print("Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros")
print("y otra función que calcule el área de un círculo recibiendo el radio del mismo.")

# ========================================================

def triangle(a,b):
    result = (a * b) / 2
    return "{:6.2f}".format(result)
# ====================
def circle(a):
    import math
    result = math.pow(a,2)
    result *= math.pi
    return "{:6.2f}".format(result)
# ====================

print()

print("Triángulo")
alto = input("Escribir la altura del triángulo: ")
alto = float(alto)
base = input("Escribir la base del triángulo: ")
base = float(base)
print("El área del triángulo es:",triangle(alto,base))

print()

print("Círculo")
radio = input("Escribir el radio del círculo: ")
radio = float(radio)
print("El área del círculo es:", circle(radio))

