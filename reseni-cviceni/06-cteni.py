# 1 Výplata přesněji (to dáš)
# Zatím jsme výplatu počítali za předpokladu,
# že každý měsíc odpracujeme stejný počet hodin, což není příliš realistické.
# Vytvořte proto textový soubor vykaz.txt, který bude obsahovat 12 řádků a na
# každém řádku počet odpracovaných hodin za každý měsíc za poslední rok.

# Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz.
# Vytiskněte tento seznam na konzoli funkcí print() abyste si ověřili, že jste soubor načetli správně.
# Nechte uživatele zadat na příkazovém řádku hodinovou mzdu.
# Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.

with open('data/vykaz.txt', encoding='utf-8') as soubor:
    hodiny = soubor.readlines()


hodina_mzda = int(input('Zadej hodinovou mzdu: '))

platy = [int(mesic) * hodina_mzda for mesic in hodiny]

# platy = []
# for mesic in hodiny:
#     platy.append(int(mesic) * hodina_mzda)

vydelek_rok = sum(platy)
prumerny_mesicni_plat = vydelek_rok / 12

print(vydelek_rok)
print(prumerny_mesicni_plat)


# 2 Počet slov (zapni hlavu)
# Stáhněte si odevzdanou slohovou práci.
# Zadání bylo sepsat text o nejméně 150ti slovech pojednávající o našem hlavním městě.
# Napište program, který spočítá počet slov v tomto textu, abychom věděli, zda bylo zadání formálně splněno.

# Nechte se vést následujícím návodem.

# Nechte váš program otevřít soubor a načíst jednotlivé řádky do seznamu.
# Každý řádek převeďte na seznam slov. Slovem se rozumí vše, co je odděleno mezerou nebo novým řádkem.
# Vypište na výstup seznam hodnot udávající počty slov na každém řádku.
# Vypište na výstup celkový počet všech slov v souboru.

with open('data/praha.txt', encoding='utf-8') as soubor:
    radky = soubor.readlines()

print(radky)
radky_slov = [radek.split() for radek in radky]
print(radky_slov)
radky_pocet_slov = [len(radek.split()) for radek in radky]
print(radky_pocet_slov)

print(sum(radky_pocet_slov))


# Bonus

# 3 Půjčovna (zavařovačka)

# Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ.
# Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů.
# V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok.
# Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

# V souboru s daty je ještě jeden problém, který není na první pohled vidět.
# Dá se vyřešit pomocí list comprehension s podmínkou uvedeném v předchozím čtení na doma.

# Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem replace().

# NEDELALI JSME - https://kodim.cz/kurzy/python-data/zaklady-programovani/prvni-programy/moduly
# Upravte váš program tak, aby jméno souboru k otevření dostal na příkazové řádce,
# abychom mohli takto zpracovávat výkazy z různých souborů, aniž bychom museli upravovat samotný kód programu.

with open('data/auta.txt', encoding='utf-8') as soubor:
    radky = soubor.readlines()

modifikovane_radky = []
for radek in radky:
    if radek.strip() != '': # pokud radek obsahuje alespon jeden 'nebily' znak
        hodnoty = radek.split(' ')
        # spz, km = radek.split(' )
        spz = hodnoty[0]
        km = float(hodnoty[1].replace(',', '.'))
        modifikovane_radky.append([spz,km])

jen_km = [radek[1] for radek in modifikovane_radky]

km_celkem = sum(jen_km)
print(km_celkem)


# osklivy one liner pomoci list comprehension
print(f"{sum([float(radek.split()[1].replace(',','.')) for radek in radky if radek.strip() != ''])} tisic kilometru")
