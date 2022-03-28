def crear_dir(dir):
    f = open(dir,'w')
    f.close()

def guardar_fichero(dir,texto):
    f = open(dir, 'w')
    f.write(texto)
    f.close()

def leer_fichero(dir):
    print("texto presente en el fichero:")
    f = open(dir, 'r')
    result = f.read()
    f.close()
    return result

def main():
    print("En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, \nlo abráis y escribáis dentro del archivo. \nPara ello, tendréis que acceder dos veces al archivo creado.")
    texto = input("Escribir un texto: ")
    texto = str(texto)
    print()
    directorio = input("Como quieres que se llame el archivo? ")
    directorio = str(directorio)
    print()
    if directorio.endswith('.txt') == False:
        directorio += '.txt'

    crear_dir(directorio)

    guardar_fichero(directorio, texto)

    print(leer_fichero(directorio))


if __name__ == '__main__':
    main()