# Pasažéři
# Autobus mezi Zdebudevsí a Kozoprdy jezdí čtyřikrát denně každý všední den v týdnu.
# Za poslední týden jsme naměřili počty pasažérů pro každou jízdu tam i zpět.
# Data jsou uložená v souboru pasazeri.txt.
# Jízda vždy obsahuje dvě čísla oddělená čárkou, která udávají počet pasažérů směrem tam a směrem zpět.

# Napište program, který pro první den vypíše, kolik pasažérů jelo celkem směrem tam a kolik směrem zpět.
# Nechť váš program vypisuje součty pasažérů ze celý týden, tedy kolik lidí za celý týden jelo směrem tam a kolik směrem zpět.

with open('data/pasazeri.txt', encoding='utf-8') as soubor:
    dny = soubor.readlines()

def cesty_tam_zpet(jizdy):
    tam = sum([int(jizda[0]) for jizda in jizdy])
    zpet = sum([int(jizda[1]) for jizda in jizdy])
    return tam,zpet

celkem_tam = 0
celkem_zpet = 0
for den in dny:
    jizdy = [jizda.split(',') for jizda in den.split(' ')]
    tam, zpet = cesty_tam_zpet(jizdy)
    celkem_tam += tam
    celkem_zpet += zpet

print(f'Tam: {tam}\tZpet: {zpet}')

# Přeznámkování
# Univerzita pro celoživotní vzdělávání se rozhodla změnit svůj známkovací systém z číselných známek 1 až 5 na hodnocení písmeny A až F.
# Bohužel změna se odehrála jaksi uprostřed semestru, takže je potřeba změnit aktuální výkazy o známkách z čísel na písmena.
# Nechte se vést následujícím postupem.

# Otevřete si dokument s jedním výkazem známek.
# Zkopírujte si tuto tabulku do textového souboru.
# Napište program, který tuto tabulku načte ze souboru a změní všechny známky tak, že 1 bude A, 2 bude B, 3 bude C, 4 bude D a 5 bude F.
# Vypište váš výsledek do nějakého souboru tak, aby se z něj dal zase zkopírovat do tabulky Google.

# TODO: Tohle byl domaci ukol

# Karty 2
# Napište program, který vylosuje seznam 4 náhodných hracích karet podobně jako v úložce Karty 1 z minulé lekce.
# Můžeme si představovat, že rozdáváme karty například v pokeru.
# Zatím pro jednoduchost nebudeme řešit, že se nám může nějaká karta v seznamu opakovat.

# Vymyslete, jak budete vylosovanou kartu v seznamu reprezentovat. Vypište pak tento seznam na výstup.
# Dále k tomuto seznamu vypište součet hodnot všech vylosovaných karet. Položme hodnotu karet J, Q a K rovnu deseti a eso rovnu jedné.

import random

def nahodna_karta():
    barvy = ['kříže', 'srdce', 'piky','káry']
    hodnoty = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    barvy_index = random.randint(0, len(barvy)-1)
    hodnoty_index = random.randint(0, len(hodnoty)-1)
    return barvy[barvy_index], hodnoty[hodnoty_index]

def hodnota_karty(karta):
    if karta == 'A' or karta == 'eso':
        return 1
    if karta.isnumeric():
        # pokud je karta sring ciselny
        return int(karta)
    # slova maji krome esa hodnotu vzdy 10
    return 10

karty = [nahodna_karta() for i in range(4)]
soucet = sum([hodnota_karty(karta[1]) for karta in karty])
print(karty)
print(soucet)

# Karty 3
# Zkusme vyřešit problém losování karet tak, aby se nám nemohlo stát,
# že nám nějaká karta padne vícekrát, když by správně v balíčku měla být od každé karty pouze jedna.

# Ze souboru karty.txt si načtěte do seznamu kompletní balíček karet.
# Zadání je stejné jako v předchozí úložce, tedy vylosovat 4 karty z balíčku a vypsat je jako seznam spolu se součtem hodnot.

# Existuje vícero možných postupů, které vedou ke stejnému výsledku.
# Zde už můžete trochu zagooglit.
# Ve většině postupů se vám bude hodit příkaz, který umí odstranit prvek seznamu na zadaném indexu:.

# x = [1, 2, 3]
# del x[0]
# print(x) # [2, 3]

# Také se vám může hodit funkce shuffle() z modulu random, která umí náhodně zamíchat seznam.

with open('data/karty.txt', encoding='utf-8') as soubor:
    karty = [line.strip().split(' ') for line in soubor.readlines()]

# myslim ze nejjednodusi je pouzit random.choices()
# https://docs.python.org/3/library/random.html#random.choices
karty = random.choices(karty, k=4)
soucet = sum([hodnota_karty(karta[0]) for karta in karty])
print(karty)
print(soucet)

