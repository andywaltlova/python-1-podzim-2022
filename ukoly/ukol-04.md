# ukol-04: Třídy

Deadline: 25.10.2022

Vyberte si kterou variantu chcete, pro odvážnější jsem sepsala jen [obecne požadavky](#obecné-požadavky-na-úkol-vyžaduje-více-času-a-vlastní-iniciativy)  třídy, atributy a metody nechávám na vás, můžete použít něco co vam přijde praktické, co vás zajímá :) Kdo se nechce zdržovat s vymášlením a chce si procvičit látku na konkretním zadání, může použít [druhou variantu](#vymyšlené-zadání).

Na úkolu si vyzkoušejte, že umíte třídu definovat a vyvořit konkrétní objekty, experimentujte. Svoje pokusy v kódu klidně nechte i při odevzdání. Pokud budete chtít něco vytvořit ale nevíte jak, jestli na to jdete dobře, nebo prostě chcete jen sdílet nápad, napiště na slack


## Obecné požadavky na úkol (vyžaduje více času a vlastní iniciativy)

- Alespoň dvě třídy, které od sebe budou dědit atributy a metody (alespoň jeden atribut a 2 metody).
- Mateřská třída by měla vždy být obecnější než třída, která některé vlastnosti a metody dědí. Podobně jako jsme měli Zaměstnanec a Brigádník (Brigádník je pouze specifická kategorie zaměstnance). Další takové vztahy mohou například být:
   - Zvíře -> Panda
   - Nemoc -> Koronavirus
   - Dopravní prostředek -> Auto.

## Vymyšlené zadání (WIP)

Uvažuj že vytváříš software pro útulek se zvířaty. Vytvoř dvě třídy `Animal` a `Dog`.

### Animal (Zvíře)
Mateřská třída, bude mít 3 atributy:
  - `name` - string, retezec (jemno zvirete)
  - `age` - int, cislo (predstavuje vek zvirete v rocich)
  - `is_alive` - bool, pravdivostni hodnota (`True` pokud je zvire nazivu, `False` pokud je po smrti), vychozi hodnota je vzdy `True`

`name` a `age` budou zaroven atributy metodu `__init__`, tedy uzivatel si je muze zvolit pri vytvareni objektu, `is_alive` je vzdy `True`

A bude mít také 2 metody:
  - `say_name(self)`
    - Vraci jmeno zvirete
  - `increase_age(self, number)`
    - Metoda zvysi atribut `age` o `number` ktere dostane jako argument

### Dog (Pes)
Tato třída dědí všechny metody a atributy ze třídy `Animal`.

Navíc ale:
  - k navratove hodnote metody `say_name(self)` pridava zvuk ktery vydava pes (woof, haf ..) a vysledek vypise pomoci `print()` (muze a nemusi take vracet upraveny vypis)
  - pridava atribute `life_expectancy` a modifikuje metodu `increase_age(self, number)` tak aby zmenila atribut `is_alive` na `False` pokud atribut `age` je vetsi nez atribut `life_expectancy`

Priklad pouziti:

```python
scooby = Dog('Scooby', 5, 10)
# stejne jako scooby = Dog('Scooby', age=5, life_expectancy=10)
scooby.increase_age(2)
print(scooby.age) # 7
print(scooby.is_alive) # True
scooby.say_name() # My name is Scooby, Woof !
scooby.increase_age(4)
print(scooby.age) # 11
print(scooby.is_alive) # False
```

---
### Bonus:
Vytvoř třetí třídu `Person` (`Osoba`). Staci kdyz bude mit atribu `name`, ale muzete si ji udelat i detailnejsi pokud chcete.

Bude mit metodu `__str__` ktera bude vracet jmeno osoby (tedy obsah atributu `name`)

Přidej třídě `Animal` atribut a metodu:
  - atribut: `owner`, který bude mít výchozí hodnotu `None`
  - metoda: `change_owner(self, owner)` - argument teto metody bude objekt tridy `Person`

Priklad pouziti:

```python
scooby = Dog('Scooby', 5, 10)
# stejne jako scooby = Dog('Scooby', age=5, life_expectancy=10)
print(scooby.owner) # 'None'

fred = Person('Fred Jones')
scooby.change_owner(fred)
print(scooby.owner.name) # 'Fred Jones'


```