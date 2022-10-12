# ukol-04: Třídy

Deadline: 25.10.2022

Vyberte si kterou variantu chcete, pro odvážnější jsem sepsala jen [obecne požadavky](#obecné-požadavky-na-úkol-vyžaduje-více-času-a-vlastní-iniciativy)  třídy, atributy a metody nechávám na vás, můžete použít něco co vam přijde praktické, co vás zajímá :) Kdo se nechce zdržovat s vymášlením a chce si procvičit látku na konkretním zadání, může použít [druhou variantu](#vymyšlené-zadání).

Na úkolu si vyzkoušejte, že umíte třídu definovat a vyvořit konkrétní objekty, experimentujte. Svoje pokusy v kódu klidně nechte i při odevzdání. Pokud budete chtít něco vytvořit ale nevíte jak, jestli na to jdete dobře, nebo prostě chcete jen sdílet nápad, napiště na slack


## Obecné požadavky na úkol (vyžaduje více času a vlastní iniciativy)

- Existuji alespoň dvě různé třídy z toho každá má:
  - alespoň 3 atributy (nemusí být všechny jako argumenty v `__init__`)
  - alespoň 3 metody + __init__ (nebo může být i `dataclass`)
- Na konci souboru je ukázka použití tříd a metod

## Vymyšlené zadání

Uvažuj že vytváříš kuchařku a potřebuješ uložit několik receptů. Vytvoř dvě třídy  `Recept` a `Kucharka` (idealne v tomto poradi).

### 1. Recept
Bude mít 3 atributy:
  - `nazev` - string, jmeno kucharky
  - `narocnost` - necham na vas jak ji budete reprezentovat (muze byt cislo, muze byt slovni vyjadreni)
  - `url_adresa` - string, odkaz na recept
  - `vyzkouseno` - bool, metoda `__init__` ji vzdy nastavi na `False`

`nazev`,`narocnost`, `url_adresa` budou atributy metody `__init__`, tedy uzivatel si je muze zvolit pri vytvareni objektu.

A bude mít také 3 metody:
  - `__str___(self)`
    - vraci hezky vypis receptu (necham na vas ktere atributy chcete do vypisu dat)
  - `zmen_narocnost(self, nova_hodnota)`
    - zmeni narocnost, tedy zmeni atribut `narocnost` na `nova_hodnota`
  - `zkusit(self)`
    - zmeni atribut `vyzkouseno` na `True`

### 2. Kucharka
Bude mít 3 atributy:
  - `nazev` - string, jmeno kucharky
  - `autor` - string, jmeno autora kucharky
  - `recepty` - list objektu tridy `Recept`, metoda `__init__` ji nastavuje vzdy na prazdny seznam `[]`

`nazev` a `autor` budou atributy metody `__init__`, tedy uzivatel si je muze zvolit pri vytvareni objektu.

A bude mít také 3 metody:
  - `__str___(self)`
    - vraci hezky vypis kucharky (necham na vas ktere atributy chcete do vypisu dat)
  - `pocet_receptu(self)`
    - vraci cislo reprezentujici pocet receptu v atributu `recepty`
  - `pridej_recept(self, recept)`
    - prida do atributu `recepty` objekt recepty ktery je v argumentu `recept`


Priklad pouziti:

```python
# Recepty
tiramisu = Recept('Tiramisu', 5, 'url-adresa')
print(tiramisu) # -> 'Tiramisu (narocnost: 5) - jeste nevyzkouseno'
muffiny = Recept('Muffiny', 3, 'url-adresa')
muffiny.zkusit()
muffiny.zmen_narocnost(2)
print(muffiny) # -> Muffiny (narocnost: 2) - vyzkouseno'

#Kucharka
moje_kucharka = Kucharka('Dezerty', 'Andy')
print(moje_kucharka) # -> 'Dezerty od Andy (0 receptu)'
moje_kucharka.pridej_recept(tiramisu)
moje_kucharka.pridej_recept(muffiny)
print(moje_kucharka.pocet_receptu()) # -> 2
```

---
### Bonus:
Pridej tride `Kucharka` metodu `vyzkousene_recepty(self)`, ktera vrati seznam receptu ktere maji atribut `vyzkouseno` `True`.

Priklad pouziti:

```python

moje_kucharka = Kucharka('Peceni', 'Andy')
print(moje_kucharka) # -> 'Peceni od Andy (0 receptu)'

pernik = Recept('Pernik', 2, 'url-adresa')
moje_kucharka.pridej_recept(pernik)
print(moje_kucharka.vyzkousene_recepty()) # => []
pernik.zkusit()
print(moje_kucharka.vyzkousene_recepty()) # => ['Pernik (narocnost: 2) - vyzkouseno']

```
