class DBK_Time:
    # atributos
    _hora = 0
    _min = 0
    _sec = 0

    #constructor
    def __init__(self, time, alarm = False):
        cadena = time.replace(":"," ").split()
        self._hora = int(cadena[0])
        self._min = int(cadena[1])
        self._sec = int(cadena[2])
        if(alarm):
            self._hora -= 1
            if(self._min == 0):
                self._min = 59
            if(self._sec == 0):
                self._sec = 60

    #toString
    def __str__(self):
        return f'{self._hora}:{self._min}:{self._sec}'

    #methods
    def rest(self, Time):
        tmp_Time = DBK_Time(str(Time))
        result = DBK_Time(str(self))
        result._hora -= tmp_Time._hora
        result._min -= tmp_Time._min
        result._sec -= tmp_Time._sec
        return result

    def passed(self,Time):
        result = DBK_Time(str(Time))
        return self._hora <= result._hora

    def correct(self,Time):
        result = DBK_Time(str(Time))
        a = 24 >= result._hora >= 0
        b = 60 >= result._min >= 0
        c = 60 >= result._sec >= 0
        return a and b and c
