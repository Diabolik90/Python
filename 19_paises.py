
def main():
    print('\nCrea un script que le pida al usuario una lista de países (separados por comas).')
    print('Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).')
    print('Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.')
    print('----------------------------------')
    paises = input("Escribir varios paises separados por comas: ")
    paises = str(paises)

    paises = paises.replace(',',' ')
    paises = sorted(paises.split(), key=str.lower)
    for i in range(len(paises)):
        paises[i] = paises[i].capitalize()

    print(f'Los paises escritos son:\n{paises}')


if __name__ == '__main__':
    main()