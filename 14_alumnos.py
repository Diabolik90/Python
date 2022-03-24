print("En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota.")
print("Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.")
print("--------------------------------------")

minimo_nota = 5

class Alumno:
    _nombre = ""
    _nota = 0

    def __init__(self, nombre):
        self._nombre = nombre

    def changeNota(self, nota):
        self._nota = nota

    def getNota(self):
        return self._nota

    def toString(self):
        print("El Alumno", self._nombre)
        if self._nota < minimo_nota:
            print("No ha aprobado con un", self._nota,"sobre 10")
        else:
            print("Ha aprobado con un", self._nota,"sobre 10")
        print()


print()

davide = Alumno("Davide")
davide.changeNota(8)

marco = Alumno("Marco")
marco.changeNota(5)

victor = Alumno("Victor")
victor.changeNota(2)

davide.toString()
marco.toString()
victor.toString()