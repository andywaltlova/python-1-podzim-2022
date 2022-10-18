# 1 Balík (zapni hlavu)
# Uvažuj, že navrhuješ software pro zásilkovou společnost.

# Vytvoř třídu Balik, která bude mít tři atributy - adresa, hmotnost a doruceno.
# První dva atributy nastav pomocí parametrů funkce __init__.
# Parametr doruceno nastav na začátku jako False.
# Připoj ke třídě funkci doruc, která změní hodnotu parametru doruceno na True.
# Přidej metodu __str__, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.
# Zkus si vytvořit nějaké objekty ze třídy Balik a ověř, že vše funguje.

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


# 2 Kniha (to dáš)
# Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů.
# Vytvoř tedy třídu Kniha, která reprezentuje knihu.
# Každá kniha bude mít atributy nazev, pocet_stran a cena. Hodnoty nastav ve funkci __init__.
# Přidej knize funkci __str__, která vypíše informace o knize v nějakém pěkném formátu.
# Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou.
# Přidej metodu sleva(), která bude mít jeden parametr - velikost slevy v procentech.
# Funkce sníží cenu knihy o dané procento.

class Kniha:
    def __init__(self, nazev, pocet_stran, cena):
        self.nazev = nazev
        self.pocet_stran = pocet_stran
        self.cena = cena

    def __str__(self):
        return f'{self.nazev} ({self.pocet_stran} stran) - {self.cena} Kc'

    def sleva(self, procenta):
        self.cena -= self.cena / procenta


kniha = Kniha('Dasenka', 200, 150)
kniha.sleva(10)
print(kniha)


# 3 Zkušební doba (zavařovačka)
# U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.

# Rozšiř metodu __init__ třídy Zamestnanec o parametr zkusebni_doba, který bude typu bool.
# Tuto hodnotu ulož jako atribut třídy Zamestnanec.
# Uprav metodu __str__. Pokud je zaměstnanec ve zkušební době, přidej k jeho/jejímu výpisu text Je ve zkušební době.

class Zamestnanec:
    def __init__(self, jmeno, pozice, zkusebni_doba):
        self.jmeno = jmeno
        self.pozice = pozice
        self.zkusebni_doba = zkusebni_doba

    def __str__(self):
        vypis = f"{self.jmeno} pracuje na pozici {self.pozice}."
        if self.zkusebni_doba:
            return vypis + ' Je ve zkušební době.'
        return vypis + ' Neni ve zkušební době.'

frantisek = Zamestnanec("František Novák", "konstruktér", False)
print(frantisek)
