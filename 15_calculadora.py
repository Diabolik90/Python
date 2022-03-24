from modulos.operaciones import *

def main():
    print("Calculadora")
    a = input("Escribir el primer número: ")
    a = float(a)
    print()

    b = 0
    while b <= 0 or b > 4:
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        b = input("Elegir una operación: ")
        b = int(b)
    print()

    c = input("Escribir el segundo número: ")
    c = float(c)
    print()

    result = 0
    match(b):
        case 1: result = suma(a,c)
        case 2: result = resta(a,c)
        case 3: result = multi(a,c)
        case 4: result = div(a,c)

    print("El resultado de tu operación es:", result)


if __name__ == '__main__':
    main()