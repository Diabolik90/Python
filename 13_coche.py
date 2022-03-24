def printAtt(**args):
    for k, v in args.items():
        print("-",v)
    print()
# =======================
print("En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:")
printAtt(a='Color',b='Ruedas',c='Puertas')
print("Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:")
printAtt(a='Velocidad', b='Cilindrada')
print("Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.")
# =======================

class Vehiculo:
    # atributos
    _color = ""
    _ruedas = ""
    _puertas = ""

    #constructor
    def __init__(self, color, ruedas, puertas):
        self._color = color
        self._ruedas = ruedas
        self._puertas = puertas

    #metodos
    def toString(self):
        print("El vehiculo es de color", self._color,", con",self._ruedas,"ruedas y",self._puertas,"puertas")


class Coche(Vehiculo):
    # atributos
    _velocidad = 0
    _cilindrada = 0

    #constructor
    def __init__(self, velocidad, cilindrada, color = "red", ruedas = 4, puertas = 5):
        super().__init__(color, ruedas, puertas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    #metodos
    def toString(self):
        super().toString()
        print("El coche tiene una velocidad máxima de", self._velocidad,"y",self._cilindrada,"de cilindrada")

print("---------------------------")
print()
myCoche = Coche(100, 1200)
myCoche.toString()
print()
otroCoche = Coche(120,2200, "verde",  puertas = "3")
otroCoche.toString()