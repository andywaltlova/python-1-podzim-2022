# 1 Házení kostkami (to dáš)
# Mějme dvě hrací kostky, kterými vždy hodíme najednou a zaznamenáme součet bodů.
# Stáhněte si textový soubor kostky.csv, který obsahuje 1000 takových nezávislých hodů.

# Načtěte tato data do tabulky a zobrazte histogram hodů.
# Zvolte vhodné rozložení přihrádek a zodpovězte následující dotazy:

# Jaká je nejčastější hodnota, která na dvou kostkách padne?
# Je větší šance, že padne hodnota 12 než že padne hodnota 2?

"""
import pandas

kostky = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/vizualizace/excs/excs>hazeni-kostkami/kostky.csv")
"""

TODO

# 2 Call centrum (to dáš)
# V souboru callcentrum.csv najdete několik tisíc záznamů pro call centrum, které udávají časy mezi jednotlivými příchozími hovory v minutách a vteřinách.
# Načtěte tato data do série v Pythonu.
# Časy převeďte na vteřiny a zobrazte jejich histogram a boxplot. Co lze z těchto dvou grafů vyčíst?

# K převodu na vteřiny můžeš použít metodu str.split().
# Pomocí ní rozdělíš hodnoty minut a vteřin do samostatných sloupců.
# Pomocí metody astype(int) převedeš hodnoty na čísla. Poté pomocí počítaných sloupců můžeš spočítat celkový počet vteřin.

"""
import pandas

callcentrum = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/vizualizace/excs/excs>call-centrum/callcentrum.csv")
callcentrum = callcentrum["hodnota"].str.split(':', expand=True).astype(int)
"""

TODO

# 3 Hurá na hory (to dáš)
# Následující data obsahují úhrnné množství sněhu (v cm) napadlé za každý rok pro posledních 50 let pro dva lyžarské resorty.
# První sloupec je rok, druhý jsou data pro resort Hora šílenství, třetí jsou data pro resort Prašné údolí.

"""
snih = [
    [1968, 480, 351],
    [1969, 462, 663],
    [1970, 443, 490],
    [1971, 518, 444],
    [1972, 537, 420],
    [1973, 446, 941],
    [1974, 446, 691],
    [1975, 450, 477],
    [1976, 356, 395],
    [1977, 381, 652],
    [1978, 345, 525],
    [1979, 430, 762],
    [1980, 266, 316],
    [1981, 533, 781],
    [1982, 471, 769],
    [1983, 407, 801],
    [1984, 526, 633],
    [1985, 391, 488],
    [1986, 361, 624],
    [1987, 470, 471],
    [1988, 506, 514],
    [1989, 333, 208],
    [1990, 462, 909],
    [1991, 438, 443],
    [1992, 364, 488],
    [1993, 452, 579],
    [1994, 484, 519],
    [1995, 460, 809],
    [1996, 465, 682],
    [1997, 431, 814],
    [1998, 463, 595],
    [1999, 460, 512],
    [2000, 503, 750],
    [2001, 462, 951],
    [2002, 429, 413],
    [2003, 405, 738],
    [2004, 477, 777],
    [2005, 385, 316],
    [2006, 368, 417],
    [2007, 513, 635],
    [2008, 448, 689],
    [2009, 525, 443],
    [2010, 427, 225],
    [2011, 460, 618],
    [2012, 417, 742],
    [2013, 517, 247],
    [2014, 466, 552],
    [2015, 523, 441],
    [2016, 422, 690],
    [2017, 420, 699]
]
snihdf = pandas.DataFrame(snih, columns=['rok', 'hora', 'udoli'])
snihdf = snihdf.set_index('rok')
"""

# Použijte krabicový graf k porovnání sněhových srážek v obou resortech.
# Do kterého byste se vypravili příští rok na lyže a proč?

TODO
