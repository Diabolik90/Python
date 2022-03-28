import pickle
from car_class import Coche

def guardar_fichero(dir, car):
    f = open(dir,'wb')
    pickle.dump(car, f)
    f.close

def leer_fichero(dir):
    f = open(dir, 'rb')
    result = pickle.load(f)
    f.close()
    return result

def main():
    print("En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, \nharéis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.")

    dir = 'class.txt'
    car = Coche(120, 2500)
    print("\nCreado:")
    print(car)

    guardar_fichero(dir,car)
    print("\nGuardado en fichero")

    print("\nLeo en fichero:")
    print(leer_fichero(dir))

if __name__ == '__main__':
    main()