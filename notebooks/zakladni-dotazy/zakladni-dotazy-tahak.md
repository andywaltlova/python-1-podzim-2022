# Tahák pro lekci Základní dotazy

## Import pandas
```
import pandas
```

## Přidání indexů
```
df.set_index("column_name")     # přeměna existujícího sloupce na index
df.reset_index()                # změna zpět na automatický číslený index
df.index                        # kontrola
```

## Výběr řádků a sloupců [metoda loc]
```
df.loc["row_index"]                 # výběr řádku
df.loc["row_index", "column_name"]  # výběr řádku a sloupce
df.loc["row_index":"row_index"]     # výběr rozsahu od:do
df.loc[["row_index_1","row_index_2"], ["column_name_1","column_name_2"]] # více řádků i sloupců
```

## Počítání nad Series
```
new_series = df["column_name"]  # vytvoření série ze sloupce
new_series.sum()                # .mean, .min, .max, .median
new_series.describe()           # informace o hodnotách v sloupcí
```

## Podmínky
```
filtered_df = df[df["column_name"] < value] # operátory ==, < , >
filtered_df = df[df["column_name"].isin(["value_1", "value_2"])]

# Řetězení více podmínek (and = &, or = |)
filtered_df = df[(df["column_name") > value) & (df["other_column_name"] == value)]

```

## Převod na DataFrame a zpět
```
new_df = pandas.DataFrame(list_name, columns = ["column_name_1", "column_name_2"] # list to DataFrame
new_df = nakupy = pandas.DataFrame(list_name) # list of dicts to DataFrame
new_list = df.to_numpy().tolist()  # DataFrame to list
```