print("Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.")

def bisiesto(y):
    a = y % 4 == 0
    b = y % 100 == 0
    c = y % 400 == 0
    if (a ^ b) or (a ^ b ^ c):
        return True
    else:
        return False
# ====================
def resultado(a):
    result = bisiesto(a)
    if(result == True):
        print(a,"es un año bisiesto")
    else:
        print(a,"no es un año bisiesto")
# ====================
print()
year = input("Escribir un año: ")
year = int(year)
resultado(year)