import random

# 1. Tombola (to dáš)
# V tombole bylo prodáno celkem 1000 lístků.
# Naším úkolem je vylosovat náhodně tři výherce.
# Napište program, který vygeneruje a vypíše tři čísla mezi 1 a 1000.
# Využijte funkci randint, nezapomeňte ale, že si ji musíte importovat z modulu random.
# Neřešte, že jedno číslo může být vygenerováno dvakrát.

for i in range(3):
    print(random.randint(1, 1000))

# Slo by i pridat cisla do listu a pak vypsat list
vyherci = []
for i in range(3):
    vyherci.append(random.randint(1, 1000))
print(vyherci)


# 2 Dělitelnost více čísly (to dáš)
# Vypišme si čísla z nějakého rozsahu na základě jejich dělitelnosti dvěma čísly.

# Zkuste z nějakého rozsahu čísel vypsat čísla, která jsou dělitelná 3 i 4 současně.
# Zkuste z nějakého rozsahu čísel vypsat čísla, která jsou dělitelná 5 nebo 6. Stačí vypsat text: "Číslo je dělitelné 5 nebo 6."

for num in range(40):
    delitelne_tremi = num % 3 == 0  # tedy zbytek po deleni je 0
    delitelne_ctyrmi = num % 4 == 0
    if delitelne_tremi and delitelne_ctyrmi:
        print(i)

for num in range(40):
    delitelne_peti = num % 5 == 0
    delitelne_sesti = num % 6 == 0
    if delitelne_peti or delitelne_sesti:
        print(f'"Číslo {num} je dělitelné 5 nebo 6."')

# 3 Seznam hostů na party (to dáš)
# Vraťte se k příkladu se zadáváním seznamu hostu na párty a zkopírujte si kód k sobě do editoru.
# Upravte program tak, že pokud uživatel v průběhu zadávání jmen napíše "konec", cyklus na zadávání jmen se ukončí.

# ! Pozoro tohle je na latku v https://kodim.cz/kurzy/uvod-do-progr-2/bonusy/cykly-2/preruseni-cyklu , kterou jsme si na lekci nerikali

# Puvodni kod z https://kodim.cz/kurzy/uvod-do-progr-2/bonusy/cykly-2/cyklus-s-ciselnou-radou
# number_of_guests = int(input("Zadej počet hostů: "))
# guest_list = []
# for i in range(number_of_guests):
#     new_guest = input("Zadej jméno hosta: ")
#     guest_list.append(new_guest)
# print(guest_list)

# Upraveny

number_of_guests = int(input("Zadej počet hostů: "))
guest_list = []
for i in range(number_of_guests):
    new_guest = input("Zadej jméno hosta nebo 'konec' pro ukonceni seznamu: ")
    if new_guest == 'konec':
        break
    else:
        guest_list.append(new_guest)
print(guest_list)

# Bonusy
# 4 Prvočíslo (zavařovačka)
# Požádej uživatele o zadání celého čísla. Následně urči, zda je toto číslo prvočíslo.

# Prvočíslo je číslo, které je dělitelné beze zbytku pouze 2 čísly - 1 a sebou samotným.

# Například 5 je prvočíslo, protože je dělitelná pouze 1 a 5.
# Naopak 4 není prvočíslo, protože je dělitelná 1, 2 a 4.

num = int(input("Zadej cislo: "))
je_prvocislo = True

if num > 1:
    # kontrola nasobku (delitelnosti cisel ktere jsou mensi nez cislo samotne ale vetsi nez 1)
    for i in range(2, num):
        # Pokud je delitelne nejakym cislem z rozsahu
        if (num % i) == 0:
            je_prvocislo = False
            # nemusime zkouset dal, uz vime ze neni prvocislo
            break

if je_prvocislo:
    print('Je prvocislo')
else:
    print('Neni prvocislo')


