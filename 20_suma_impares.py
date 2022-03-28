from functools import reduce

def set_list():
    numbers = input("Escribir una lista de numeros separados por comas: ")
    numbers = str(numbers)
    numbers = numbers.replace(',',' ').split()
    # delete duplicated
    numbers = list(set(numbers))
    #convert to int
    result = []
    for i in range(len(numbers)):
        result.append(int(numbers[i]))
    # order the numbers
    result = sorted(result)
    return result

def set_odd(a):
    result = list(filter(lambda x: x % 2, a))
    return result

def sum(x):
    result = reduce(lambda a,b: a + b, x)
    return result

def main():
    print('\nEn este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista')
    print('pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.')
    print('----------------------------------')

    # input
    numbers = set_list()
    print(f'Tus números son: {numbers}')

    # only odd
    numbers = set_odd(numbers)
    print(f'Los números impares son: {numbers}')

    # sum odd numbers
    numbers = sum(numbers)
    print(f'La suma total de los números es: {numbers}')


if __name__ == '__main__':
    main()