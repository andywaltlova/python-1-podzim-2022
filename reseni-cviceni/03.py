# 1 Násobení (to dáš)
# Napiš funkci mult, která bude mít dva číselné parametry.
# Funkce oba parametry vynásobí a vrátí výsledek.

def mult(a: int, b: int):
    vysledek = a * b
    return vysledek

# print(mult(1, 3))


# 2 Hotel (to dáš)
# Napiš funkci total_price, která vypočte cenu noci v hotelu.
# Funkce bude mít dva parametry - persons a breakfast.
# Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč.
# Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

# Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).


def total_price(persons, breakfast=False):
    night_price = 850
    breakfast_price = 125

    nights_total = night_price * persons
    breakfast_total = 0
    if breakfast:
        breakfast_total += breakfast_price * persons
    return nights_total + breakfast_total

# print(total_price(10, False))

# Uplne genialni kod co vymyslela Paja Vencovska
def total_price(persons, breakfast=False):
    breakfast *= 125 * persons
    persons *= 850
    return breakfast + persons

# print(total_price(persons=10, breakfast=False))

# Nebo jeste jina varianta

def total_price(persons, breakfast=False):
    total_price = 850
    if breakfast:
        total_price += 125
    return persons * total_price


# Bonusy

# 3 Měsíc narození (zapni hlavu)
# Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo.
# Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup.
# Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.
# Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.

def month_of_birth(number):
    month = int(str(number)[2:4])
    if month > 12:
        month -= 50
    return month


# print(month_of_birth(9555125899))


# 4 Ruleta (smrt v přímém přenosu)
# Napiš funkci, která bude jednoduchou simulací rulety.
# Budeme uvažovat pouze možnost sázení na řady.
# Uživatel si může vybrat jednu ze tří řad:

# první řada (hodnoty 1, 4, 7 atd.),
# druhá řada (hodnoty 2, 5, 8 atd.),
# třetí řada (hodnoty 3, 6, 9 atd.).

# Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky.

# Vytvoř funkci roulette, která bude mít parametry číslo řady a výši sázky.
# Pomocí funkce randint z modulu random vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36.
# Vyhodnoť, do které řady číslo náleží. Nezapomeň, že 0 nepatří do žádné z řad a pokud padne,
# uživatel vždy prohrává.

# Funkce roulette vrací hodnotu výhry.
# Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky,
# v opačném případě nevyhrává nic jeho sázka propadá.


# import random
from random import randint


def roulette(rada, sazka):
    cislo = randint(0, 36)

    trefil_1 = rada == 1 and cislo % 3 == 1
    trefil_2 = rada == 2 and cislo % 3 == 2
    trefil_3 = rada == 3 and cislo % 3 == 0

    # Taky moznost
    # trefil_1 = rada == 1 and cislo in range(1, 36, 3)
    # trefil_2 = rada == 2 and cislo in range(2, 36, 3)
    # trefil_3 = rada == 3 and cislo in range(3, 36, 3)

    if trefil_1 or trefil_2 or trefil_3:
        return sazka * 2

    return 0

def roulette(rada, sazka):
    # Reseni se slovnikem a modifikovanou podminkou
    cislo = randint(0, 36)
    rady = {
        1: rada == 1 and cislo % 3 == 1,
        2: rada == 2 and cislo % 3 == 2,
        3: rada == 3 and cislo % 3 == 0
    }

    if rady.get(rada, False):
        return sazka * 2
    return 0

def roulette(rada, sazka):
    # Reseni i s vypisy

    cislo = randint(0, 36)
    if cislo == 0:
        print('Nula nevyhrava :(')
        return cislo

    zbytek = cislo % 3
    rady = {
        1: rada == 1 and zbytek == 1,
        2: rada == 2 and zbytek == 2,
        3: rada == 3 and zbytek == 0
    }

    # Asi bych tady pouzila inline podminku a vyuzila ze ty zbytky odpovidaji radam krome te treti
    print(f'Cislo {cislo} patri do {3 if zbytek == 0 else zbytek} rady.')

    if rady.get(rada, False):
        vyhra = sazka * 2
        print(f'Vyhravas {vyhra}!')
        return sazka * 2

    print(f'Nevyhravas protoze sis tipnul {rada} radu.')
    return 0

roulette(1, 100)