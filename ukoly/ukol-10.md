# ukol-10: Zaměstnanci a Projekty

## Zaměstnanci

Uvažuj, že zpracováváš analýzu pro softwarovou firmu. Firma má kanceláře v Praze, Plzni a Liberci. Seznam zaměstnanců pro jednotlivé kanceláře najdeš v souborech [zam_praha.csv](data/zam_praha.csv), [zam_plzeň.csv](data/zam_plzeň.csv) a [zam_liberec.csv](data/zam_liberec.csv).

```
import requests

r = requests.get("https://github.com/andywaltlova/python-1-podzim-2022/blob/master/ukoly/data/zam_praha.csv")
open("zam_praha.csv", "wb").write(r.content)

r = requests.get("https://github.com/andywaltlova/python-1-podzim-2022/blob/master/ukoly/data/zam_plzeň.csv")
open("zam_plzeň.csv", "wb").write(r.content)

r = requests.get("https://github.com/andywaltlova/python-1-podzim-2022/blob/master/ukoly/data/zam_liberec.csv")
open("zam_liberec.csv", "wb").write(r.content)

r = requests.get("https://github.com/andywaltlova/python-1-podzim-2022/blob/master/ukoly/data/platy_2021_02.csv")
open("platy_2021_02.csv", "wb").write(r.content)
```

* Načti data o zaměstnancích z CSV souborů do tabulek (DataFrame). Ke každé tabulce přidej nový sloupec mesto, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.
* Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.
* Ze souboru [platy_2021_02.csv](data/platy_2021_02.csv) načti platy zaměstnanců za únor 2021. Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.
* Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor, znamená to, že v naší firmě již nepracuje.
* Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.


**Dobrovolný doplněk**

* Ulož do proměnné počet zaměstnaců, kteří v naší firmě již nepracují.
* V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují. Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují. Tabulku ulož do souboru CSV.



## Projekty
Pokračuj ve své práci pro softwarovou firmu. Ze souboru [vykazy.csv](data/vykazy.csv) načti informace o výkazech na projekty pro jednoho vybraného zákazníka.

```
import requests

r = requests.get("https://github.com/andywaltlova/python-1-podzim-2022/blob/master/ukoly/data/vykazy.csv")
open("vykazy.csv", "wb").write(r.content)
```

* Načti data ze souboru a ulož je do tabulky.
* Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.

**Dobrovolný doplněk**

Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení. 

Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře, tj. spočítej celkový počet hodin vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka.



# BONUS
## Teplota ve městech podruhé

Pokračuj ve své práci s informacemi o průměrných teplotách. Pokud jsi zpracovala pokročilou variantu, můžeš pracovat s teplotami ve stupních Celsia.

Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky. Dále napiš následující dotazy:

1. Dotaz na řádky z 13. listopadu 2017 (sloupec `Day` musí mít hodnotu 13).
1. Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec `Day` musí mít hodnotu 13 a sloupec `Country` hodnotu US). Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
1. Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec `City`) Washington a Philadelphia.
1. Vrať se k pomocné tabulce, kterou jsi vytvořila v bodu 2. Vypiš průměrnou hodnotu ze všech měření, která byla provedena 13. listopadu 2017 na území Spojených států amerických. K tomu využij funkci `.mean()`, která funguje stejně jako funkce `.sum()`, kterou jsme si ukazovali na lekci. Pokud znáš základy statistiky, zkus funkci pro medián `.median()` a rozptyl `.var()`.
