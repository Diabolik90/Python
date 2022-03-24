print("Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.")

lista = []

for i in range(1,101):
    lista.append(i)

revLista = sorted(lista, reverse = True)

print(revLista)