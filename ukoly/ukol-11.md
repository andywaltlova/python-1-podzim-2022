# ukol-11: Pošta

Česká pošta má [stránku na webu](https://www.ceskaposta.cz/rady-a-navody/jak-spravne-nadepsat-zasilku), která radí, jak správně nadepsat zásilku. Uvádí i několik vzorů pro české i zahraniční zásilky.

V souboru [posta.html](data/posta.html) nalezneš zdrojový kód této stránky v HTML (to je značkovací jazyk, ve kterém jsou napsané některé webové stránky, nebo části některých webových stránek.). 

1. Soubor si načti do proměnné tak, aby se celý jeho obsah nacházel jako jeden řetězec v proměnné. Můžeš využít metodu `read()` (doplň název souboru a název své proměnné):

```py
with open(<nazev-souboru>, encoding='utf-8') as vstup:
    <nazev-promenne> = vstup.read()
```

2. Nahraď znaky odřádkování (zapisuje se jako `'\n'`) jednoduchou mezerou pomocí metody `replace()`.

3. Nahraď po sobě jdoucích víc mezer jedinou mezerou: Sestav regulární výraz, který označuje jednu nebo více mezer. Pak pomocí `re.sub()` nahraď takové sekvence jedinou mezerou. První parametr metody `re.sub()` je regulární výraz, který nahrazujeme, druhý parametr je řetězec, který nahrazujeme, a třetí parametr je řetězec, ve kterém nahrazujeme.

Příklad použití metody `re.sub`:

```py
print(re.sub('123?', 'X', 'ABC12ABCD1234'))  # ABCXABCDX4
```

4. Najdi v datech všechna česká a slovenská města a jejich PSČ, která se nacházejí v ukázkových adresách. Mají format `PSČ MĚSTO`, kde `PSČ` se skládá ze tří číslic, mezery a dvou číslic, a `MĚSTO` se skládá z jednoho, dvou nebo tří slov oddělených mezerou, za kterými může ještě následovat číslo pošty. 

Například:

```
460 15 LIBEREC 15
512 11 VYSOKÉ NAD JIZEROU
```

Celkově je potřeba identifikovat 17 adres.