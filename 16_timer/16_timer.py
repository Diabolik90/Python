import time
from clases.time_class import DBK_Time

print("En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa.")
print("Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.")
print("En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,")
print("haréis una operación para calcular el tiempo que queda de trabajo.")
print("---------------------------------------------------")

print("Calculo del tiempo")
print()

# Guardo la hora
originalTime = DBK_Time(time.asctime().split()[3])
print(f'Ahora son las {originalTime}')

#Confirmo la alarma
alarma = '19:00:00'
confirm = 0
while confirm < 1 or confirm > 2:
    print(f'Horario configurado a las {alarma}')
    print("1. Si")
    print("2. No")
    confirm = input("Confirmas? ")
    confirm = int(confirm)

# Pregunto a que hora la alarma
correct = False
if confirm == 1:
    correct = True
while not correct:
    print()
    print("A qué hora quiere salir?")
    alarma = input("Escribir [hh:mm:ss] : ")
    alarma = str(alarma)
    if(alarma.count(':') == 2):
        correct = originalTime.correct(alarma)
    if(correct == False):
        print("Digitar correctamente el horario")

# Creo la alarma
myTime = DBK_Time(alarma, True)

# Calcolo el tiempo restante
print()
if(myTime.passed(originalTime)):
    print("Ya es hora de salir!")
else:
    print(f'Tempo restante {myTime.rest(originalTime)}')






