print("Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.")
print("Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]")

start = input("Introduce el numero inicial: ")
start = int(start)

end = input("Introduce el numero final: ")
end = int(end)

lista = []
for i in range(start,end):
    if( i % 2 != 0):
        lista.append(i)

print("Los números impares son:",lista)