import time

print("En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa.")
print("Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.")
print("En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,")
print("haréis una operación para calcular el tiempo que queda de trabajo.")
print("---------------------------------------------------")

def actualTime(h, m, s):
    actual = [str(h), str(m), str(s)]
    result = ':'.join(actual)
    return 'Son las ' + result

def restTime(h, m, s):
    if h < 0:
        return 'Ya es hora de salir!'
    else:
        rest = [str(h), str(m), str(s)]
        result = ':'.join(rest)
        return 'Tempo restante ' + result


print("Calculo del tiempo")
print()

# Guardo la hora
tiempo = time.asctime().split()[3].replace(":"," ").split()

# Convierto el tipo
hora = int(tiempo[0])
min = int(tiempo[1])
sec = int(tiempo[2])

# Imprimo el resultado
actual = actualTime(hora, min, sec)
print(actual)

# Pregunto a que hora la alarma
alarma = input("A qué hora quiere salir? ")
alarma = int(alarma)
alarma -= 1

# Calculo el tiempo restante
print()
print(restTime(alarma-hora, 59 - min, 60 - sec))


