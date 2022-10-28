# 1 Předčíslí u čísla účtu (pohodička)
# Přidej k regulárnímu výrazu na číslo účtu možnost předčíslí, tj. na začátku může být 0 až 6 čísel a za nimi může (ale nemusí) být pomlčka.

TODO

# 2 Číslo účtu podruhé (pohodička)
# Nejmenovaná česká banka rozlišuje typy účtů podle číslic na začátku čísla.
# Například je-li první číslice 1, jedná se o investiční účet, je-li první číslice 2, jde o bankovní účet.
# Uvažujme, že naše tajemná banka má kód (poslední čtyři čísla) 2100.

# Uprav regulární výraz (nemusíš řešit předčíslí) tak, aby na prvním místě mohla být pouze 1 nebo 2.
# Uvažuj, že na druhém místě mohou být jen číslice 0, 1 nebo 2.

TODO

# 3 Registrační značka (zapni hlavu)
# Standardní registrační značky automobilů, vydané od roku 2004, mají následující formát:

# Na prvním místě je číslo.
# Na druhém místě písmeno, které označuje kraj.
# Na třetím místě je číslo nebo písmeno.
# Na čtvrtém místě je mezera a následuje čtveřice čísel.
# Napiš regulární výraz, který bude kontrolovat formát registrační značky.
# Ověřit si ho můžeš na následujících značkách, které mají správný formát.

"""
4A6 8244
6B2 6635
2AD 3824
7C1 5025
"""

# Značky níže mají špatný formát.
"""
AC8 5484
924 1541
8A2 25C2
3P 4564
1A 25364
"""

# Zkus nyní regulární výraz ještě zdokonalit a povol na druhém místě pouze znak, který označuje nějaký konkrétní kraj.
# Platné znaky na druhém místě tedy budou tyto: A, B, C, E, H, J, K, L, M, P, S, T, U, Z.

TODO

# 4 Telefonní číslo (zapni hlavu)
# V Česku máme standardně devítimístná telefonní čísla. Napiš regulární výraz, který sedí na "naše" telefonní čísla.

# Často se telefonní číslo rozděluje na trojice, které jsou odděleny mezerou.
# Uprav svůj výraz tak, aby odpovídal číslům s mezerou i bez mezery.
# Před telefonní číslo je výhodné přidat mezinárodní předvolbu (v našem případě +420), aby nám mohli volat i lidé ze zahraničí.
# Přidej to ke svému regulárnímu výrazu.

TODO

# 5 Ministerstva (zapni hlavu)
# Napiš regulární výraz, který z následujícího řádku vybere celé názvy ministerstev.

"""
Ministerstvo pro místní rozvoj, Celní správa České republiky, Ministerstvo životního prostředí, Ministerstvo práce a sociálních věcí, Český statistický úřad, Nejvyšší kontrolní úřad
"""

# 6 Nápravy (to dáš)
# Uvažuj vyhlášku, která definuje maximální hmotnosti vozidel u trojnápravy nákladních vozidel a jejíž zjednodušený text je níže.
# Napiš 2 regulární výraz. Prvním zjistíš limit (nebo limity) vzdáleností náprav v metrech a druhým maximální povolenou hmotnost v tunách.

# Maximální hmotnosti trojnápravy při dílčím rozvoru náprav jsou:

# do 1,3 m včetně - 21,00 t,
# nad 1,3 m do 1,4 m včetně - 24,00 t,
# nad 1,4 m do 1,8 m včetně - 27,00 t,

TODO


# 7 Slavný soude (to dáš)
# Spisová značka, tj. označení spisu u soudu, má zpravidla následující formát:

# číslo soudního oddělení (např. 1 až 2 čísla),
# rejstříková značka (např. jedno až tři velká písmena),
# běžné číslo, podle toho kdy k soudu věc přišla (např. 1 až 4 čísla),
# lomítko a za ním ročník (4 čísla).
# Může vypadat například takto: 63 C 397/2014. Napiš regulární výraz a na tomto příkladu jej vyzkoušej.

TODO

# 8 Ave, Caesar! (zapni hlavu)
# Římské číslice se dodnes používají například pro označení století, pořadí panovníků, papežů atd. Zkus sestavit regulární výraz, který zachytí římské číslice v následujících řetězcích. Nemusíš vytvářet obecný regulární výraz pro římské číslice, ale pouze výraz, který bude fungovat na dané řetězce.

"""
IX. století
Matematika pro VII. třídu
Star Trek III
Karel IV.
papež Benedict V.
Bělá je X. část statutárního města Děčín.
III. patro
II. stupeň povodňové aktivity
Konstantin XI. Dragases
"""
