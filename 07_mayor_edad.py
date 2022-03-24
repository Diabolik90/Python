print("Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.")

edad = input("Introduce tu edad: ")
edad = int(edad)

mayor = 18

if edad >= mayor:
    print("Usted es mayor de edad")
else:
    print("Usted no es mayor de edad")