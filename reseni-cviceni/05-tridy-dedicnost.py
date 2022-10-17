# 1 Částečný úvazek (zapni hlavu)
# Naše firma se rozhodla zaměstnávat i pracovníky na částečné úvazky, pro které bude vytvořena zvláštní třída.
# Vytvoř novou třídu Brigadnik, která bude dědit od třídy Zamestnanec a bude mít navíc atribut uvazek,
# který reprezentuje velikost úvazku oproti plnému.
# Přidej informaci o úvazku k výpisu informací do funkce __str__.

# TODO

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
        vypis = f'{self.adresa}({self.hmostnos} kg) - {self.doruceno}'
        return vypis

# Vytvoř třídu CennyBalik, která dědí od třídy Balik.
# CennyBalik má navíc atribut hodnota, ostatní atributy dědí od třídy Balik.
# Atribut hodnota nastav pomocí funkce __init__. Ostatní parametry předej funkci __init__ třídy Balik.
# Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí.

# TODO
