# 1 Seznamy čísel (pohodička)
# Mějme zadaný následující seznam

cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
# Vytvořte seznam, který obsahuje

# každé z čísel ze seznamu cisla vynásobené dvěma,
# každé z čísel ze seznamu cisla s opačným znaménkem,
# každé z čísel ze seznamu cisla umocněné na druhou,
# každé z čísel ze seznamu cisla jako řetězec.

vynasobene_dvema = [cislo*2 for cislo in cisla]
opacne_znamenko = [cislo*(-1) for cislo in cisla]
umocnene = [cilso**2 for cislo in cisla]
retezce = [str(cislo) for cislo in cisla]


# 2 Seznamy řetězců (to dáš)
# Mějme zadaný následující seznam

jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

# Vytvořte seznam, který obsahuje

# počty písmen ve všech jménech,
# všechna jména napsaná velkými písmeny,
# všechna jména plus písmeno 'a' na konci (stanou se z nich tedy ženská jména),
# všechna jména převedená na malá písmena s koncovkou '@email.cz'.

pocty = [len(jmeno) for jmeno in jmena]
velka = [jemno.upper() for jmeno in jmena]
zenska = [jmeno + 'a' for jmeno in jmena]
email = [jmeno.lower() +'@email.cz' for jmeno in jmena]


# 3 Seznam teplot (zapni hlavu)
# Mějme zadaný následující seznam naměřených teplot.
# Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# Vytvořte seznam průměrných teplot pro každý den.
# Vytvořte seznam ranních teplot.
# Vytvořte seznam nočních teplot.
# Vytvořte seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
# Spočítejte celkovou průměrnou teplotu za celý týden.

prumery = [sum(den)/len(den) for den in teploty]
rano = [den[0] for den in teploty]
vecer = [den[3] for den in teploty]
poledne_noc = [[den[1], den[3]] for den in teploty]
tydeni_prumery = sum(prumery)/len(prumery)
