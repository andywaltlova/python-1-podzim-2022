class Zamestnanec:
    def __init__(self, jmeno: str, pozice: str):
        self.jmeno = jmeno
        self.pozice = pozice
        self.pocet_dni_dovolene = 25

    def __str__(self):
        return f'{self.jmeno} pracuje na pozici {self.pozice}'

    def cerpani_dovolene(self, pocet_dni):
        if pocet_dni <= self.pocet_dni_dovolene:
            self.pocet_dni_dovolene -= pocet_dni
            return f'Zbyva dovolene: {self.pocet_dni_dovolene}'
        else:
            return f'Nemas dostatek dovolene: {self.pocet_dni_dovolene}'

class Manazer(Zamestnanec):
    def __init__(self, jmeno, pocet_podrizenych):
        super().__init__(jmeno, 'Manazer')
        self.pocet_dni_dovolene = 30
        self.pocet_podrizenych = pocet_podrizenych

    def __str__(self):
        return f'{super().__str__()} a ma {self.pocet_podrizenych} podrizenych'

martin = Manazer('Martin', 5)
print(martin.cerpani_dovolene(10))
print(martin)

