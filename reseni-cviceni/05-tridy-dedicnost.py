# 1 Částečný úvazek (zapni hlavu)
# Naše firma se rozhodla zaměstnávat i pracovníky na částečné úvazky, pro které bude vytvořena zvláštní třída.
# Vytvoř novou třídu Brigadnik, která bude dědit od třídy Zamestnanec a bude mít navíc atribut uvazek,
# který reprezentuje velikost úvazku oproti plnému.
# Přidej informaci o úvazku k výpisu informací do funkce __str__.

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

class Brigadnik(Zamestnanec):
    def __init__(self, jmeno, pozice, uvazek):
        super().__init__(jmeno, pozice)
        self.uvazek = uvazek

    def __str__(self):
        return f'{super().__str__()} a ma uvazek {self.uvazek}'


matej = Zamestnanec('Matej', 'programator')
print(matej)
michal = Brigadnik('Michal', 'programator', 0.5)
print(michal)


# 2 Balík (zapni hlavu)
# Pokračuj ve své práci pro zásilkovou společnost. Společnost nově doručuje i cenné balíky, které mají zadanou určitou hodnotu.

# Trida Balik z minuleho cviceni
class Balik:
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False

    def doruc(self):
        self.doruceno = True

    def __str__(self):
        vypis = f'{self.adresa}({self.hmotnost} kg) - {self.doruceno}'
        return vypis

# Vytvoř třídu CennyBalik, která dědí od třídy Balik.
# CennyBalik má navíc atribut hodnota, ostatní atributy dědí od třídy Balik.
# Atribut hodnota nastav pomocí funkce __init__. Ostatní parametry předej funkci __init__ třídy Balik.
# Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí.


class CennyBalik(Balik):
    def __init__(self, adresa, hmotnost, hodnota):
        super().__init__(adresa, hmotnost)
        self.hodnota = hodnota

    def __str__(self):
        return f'{super().__str__()} [{self.hodnota} Kc]'

print(drahy_balicek)


