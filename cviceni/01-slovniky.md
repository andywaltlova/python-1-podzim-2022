# 1. Vysvědčení
Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota známka z daného předmětu. Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematiku a dějepis). Vypiš obsah slovníku pomocí funkce `print()`.

```python
#TODO
```

# 2. Detektivky
Vydavatel detektivek si eviduje prodané kusy u jednotlivých knih. V následujícím slovníku najdeš tři knihy a u každé z nich je počet prodaných kusů.

```python
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
```

- Zkopíruj si slovník do svého programu.
- Přidej do slovníku nově vydanou detektivku "Noc, která mě zabila", která zatím nebyla uvedena na trh, je tedy prodáno 0 kusů.
- U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100.

```python
#TODO
```

# 3. Tombola
V následujícím slovníku jsou uložena čísla lístků tomboly a příslušné výhry.

```py
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
```
- Napiš program, který se nejprve zeptá uživatele na číslo jeho lístku. Vstup uživatele si převeď na int!
- Zkontroluj, zda je číslo lístku ve slovníku. Pokud ne, vypiš text "Bohužel nevyhráváš nic." Pokud číslo ve slovníku je, vypiš uživateli, co vyhrál.
- Odeber výhru pro daný lístek ze slovníku, abychom tam evidovali pouze nevydané ceny.

```python
#TODO
```

# 4. Paranoidní večírek (Bonus)

Pořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl, že každý z hostů bude mít speciální heslo, které je platné jen pro něj. Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost. Hostu na seznamu, který zadá správné heslo, vypíše program text: "Smíš vstoupit."

```python
passwords = {
    "Jiří": "tajne-heslo",
    "Natálie": "jeste-tajnejsi-heslo",
    "Klára": "nejtajnejsi-heslo"
}
```

```python
#TODO
```