print("Escribe una función que pueda decirte si un número (número entero) es primo o no.")

def numero_primo(a):
    for i in range(2,a):
        if a % i == 0:
            return True

    return False
# ====================
def resultado(a):
    result = numero_primo(a)
    if(result == False):
        print(a,"es un número primo")
    else:
        print(a,"no es un número primo")
# ====================

print()
number = input("Escribir un número entero: ")
number = int(number)
resultado(number)
