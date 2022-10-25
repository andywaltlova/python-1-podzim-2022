# 1 Rozepsaná výplata (to dáš)
# Modifikujte program pro počítání výplaty z předchozí sekce tak,
# aby nevypisoval průměrnou výplatu za rok, nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.

# Nejprve tyto informace vypište na výstup pomocí funkce print().
# Poté program upravte tak, aby vypsal tyto výsledky do souboru.

with open('data/vykaz.txt', 'r', encoding='utf-8') as vstup:
    radky = [int(radek) for radek in vstup.readlines()]

hodinova_mzda = 250
platy = [hodinova_mzda*mesic for mesic in radky]

# for mesic in radky:
#     print(mesic * hodinova_mzda)

print(platy)
platy_k_zapisu = [str(plat) + '\n' for plat in platy]

with open('data/mesicni_platy.txt', 'w', encoding='utf-8') as vystup:
    # for plat in platy:
    #     vystup.write(f'{plat}\n')
        # vystup.write(str(plat) + '\n')
    vystup.writelines(platy_k_zapisu)


# 2 Hody kostkou (zapni hlavu)
# Napište program, který vytvoří seznam deseti náhodných hodů dvanáctistěnnou kostkou.

# Nejdříve tento seznam vytiskněte na konzoli pomocí funkce print().
# Upravte váš program tak, aby náhodné hody kostkou vypsal do souboru s názvem hody.txt na jeden řádek oddělené čárkou a mezerou.

# (NEDELALI JSME parametry prikazove radky https://kodim.cz/kurzy/python-data/zaklady-programovani/prvni-programy/moduly)
# Upravte váš program tak, aby počet hodů dostal jako parametr na příkazové řádce. Zkuste použitím vašeho programu vyrobit 100, 1000 a 10 000 hodů.

import random

hody = [str(random.randint(1, 6)) for i in range(10)]
print(hody)

hody_zapis = ', '.join(hody) # musi byt retezce ne cisla

with open('data/hody.txt', 'w', encoding='utf-8') as vystup:
    # for hod in hody:
    #     vystup.write(f'{hod},') # tady je trochu naprd ze i posledni cisl oza sebou bude mit carku

    vystup.write(hody_zapis)

# Bonus

# 3 Dny v měsíci (zavařovačka)
# Napište program, který bude mít přímo v kódu zapsaný počet dní v jednotlivých měsících takto:

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Nechte váš program vypsat tento seznam do souboru s názvem kalendar.txt, každé číslo na jeden řádek.
# Upravte váš program tak, aby zároveň s počtem dnů vypisoval i název měsíce. Oddělte v souboru název měsíce a počet dnů pomocí tabulátoru.
# Upravte váš program tak, aby jako první řádek výsledného souboru obsahoval nadpisy pro jednotlivé sloupce, tedy měsíc a počet dní.

with open('data/kalendar.txt', 'w', encoding='utf-8') as vystup:
    for dny in pocty_dni:
        vystup.write(f'{dny}\n')

# Mohly byste si klidne udelat i slovnik misto listu
mesice = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']

with open('data/kalendar.txt', 'w', encoding='utf-8') as vystup:
    vystup.write('Month\tDays\n') # nadpisy sloupcu
    for i in range(len(mesice)):
        vystup.write(f'{mesice[i]}\t{pocty_dni[i]}\n')
