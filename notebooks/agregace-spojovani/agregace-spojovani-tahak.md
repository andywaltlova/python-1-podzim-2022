# Tahák pro lekci Agregace a spojovaní v Pandas

## Import pandas
```
import pandas
```

## Chybějící hodnoty

* NaN
* None

### Najdi chybějící hodnoty
```
data["sloupec"].isnull()
data["sloupec"].notnull()

# True or False
```

### Odstraň chybějící hodnoty
```
data.dropna() # řádky
data.dropna(axis=1) # sloupce
```

### Nahraď chybějící hodnoty
```
data.fillna()
```

## Spojovaní dat
```
spojena_data = pandas.concat([data1, data2, data3])

# v SQL tomu odpovídá operace UNION
```

## Projování dat
```
propojena_data = pandas.merge(data1, data4, on=["sloupce"], how="outer")

# v SQL tomu odpovídá operace JOIN
```

## Agregace
```
data.groupby("sloupec").sum() 
# count, max, min, mean, median

## Agregace jen vybraných sloupců
data.groupby("sloupec")["hodnota"].sum()

## Funkce .agg()
data.groupby("sloupec").agg({"hodnota": ["max", "mean"]})
```

## Vytvoření nového sloupec
```
data["novy_sloupec"] = "hodnota"
```

## Přejmenování sloupců
```
data = data.rename(columns={"nazev_sloupce": "novy_nazev_sloupce"})
```

## Řazení
```
data.sort_values(by="sloupec")
```

## Export souboru
```
data.to_csv("soubor.csv", index=False)
```




