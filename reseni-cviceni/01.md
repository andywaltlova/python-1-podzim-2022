# ukol-01: Balíky

Hlavním cílem úkolu z první lekce je vyzkoušet si systém odevzdávání (viz [návod](../jak-na-domaci-ukoly.md)). Pokud do příští lekce
nevyřešíš úlohu, odevzdej alespoň testovací soubor, abychom věděli, že víš jak na to.

V případě dotazů vždy můžeš kontaktovat kouče ve Slackovém kanálu tvé skupinky.

---

## Zadání:
Níže máš slovník, který obsahuje kódy balíků s informací, zda již byl balík předán kurýrovi k doručení. Pokud byl předán, má hodnotu `True`,
v opačném případě má hodnotu `False`.

Napiš program pro operátora společnosti, který poskytuje informaci, zda byl balík předán kurýrovi. Nejprve se uživatele zeptej na kód balíku.
Následně podle hodnoty ve slovníku vypiš větu `Balík byl předán kurýrovi` nebo `Balík zatím nebyl předán kurýrovi`.

```py
baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
```
