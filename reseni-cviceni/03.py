# 1 Násobení (to dáš)
# Napiš funkci mult, která bude mít dva číselné parametry.
# Funkce oba parametry vynásobí a vrátí výsledek.

# 2 Hotel (to dáš)
# Napiš funkci total_price, která vypočte cenu noci v hotelu.
# Funkce bude mít dva parametry - persons a breakfast.
# Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč.
# Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

# Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).

# Bonusy

# 3 Měsíc narození (zapni hlavu)
# Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo.
# Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup.
# Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.
# Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.

# 4 Ruleta (smrt v přímém přenosu)
# Napiš funkci, která bude jednoduchou simulací rulety.
# Budeme uvažovat pouze možnost sázení na řady. Uživatel si může vybrat jednu ze tří řad:

# první řada (hodnoty 1, 4, 7 atd.),
# druhá řada (hodnoty 2, 5, 8 atd.),
# třetí řada (hodnoty 3, 6, 9 atd.).

# Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky.

# Vytvoř funkci roulette, která bude mít parametry číslo řady a výši sázky.
# Pomocí funkce randint z modulu random vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36.
# Vyhodnoť, do které řady číslo náleží. Nezapomeň, že 0 nepatří do žádné z řad a pokud padne,
# uživatel vždy prohrává.

# Funkce roulette vrací hodnotu výhry.
# Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky,
# v opačném případě nevyhrává nic jeho sázka propadá.