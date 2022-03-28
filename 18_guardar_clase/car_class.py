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

    #toString
    def __str__(self):
        return f'El vehiculo es de color {self._color}, con {self._ruedas} ruedas y {self._puertas} puertas'


class Coche(Vehiculo):
    # atributos
    _velocidad = 0
    _cilindrada = 0

    #constructor
    def __init__(self, velocidad, cilindrada, color = "rojo", ruedas = 4, puertas = 5):
        super().__init__(color, ruedas, puertas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    #toString
    def __str__(self):
        return f'{super().__str__()}. El coche tiene una velocidad máxima de {self._velocidad} y {self._cilindrada} de cilindrada'