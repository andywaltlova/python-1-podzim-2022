# 1 Převod času (pohodička)
# V proměnné apolloStart máme uložený datum a čas startu Apolla 11.
# Vypiš datum na obrazovku ve formátu, na který jsou zvyklí Američané, tj. na první místo napiš měsíc, dále den a nakonec rok, jako oddělovače použij lomítka.
# Čas vypisovat nemusíš.

from datetime import datetime

start_Apolla = datetime(1969, 7, 16, 14, 32)

start_Apolla_pro_Americany = start_Apolla.strftime("%m/%d/%Y")

print(start_Apolla_pro_Americany)


# 2 Čas od startu (zapni hlavu)
# Satelit Solar Orbiter, který má za cíl pozorování Slunce, odstartoval 10. února 2020 v 5:03. Ulož si hodnotu startu do proměnné.

# Který den v týdnu Solar Orbiter odstartoval?
# Spočítej, kolik času od jeho startu uplynulo.

# Ulož si hodnotu startu do proměnné.
start_Solar_Orbiter = datetime(2020, 2, 10, 5, 3)

# Který den v týdnu Solar Orbiter odstartoval?
den_v_tydnu = start_Solar_Orbiter.weekday()
den_v_tydnu = start_Solar_Orbiter.strftime("%A")

print(f"Solar Orbiter odstartoval v {den_v_tydnu}")

# Spočítej, kolik času od jeho startu uplynulo.
aktualni_cas = datetime.now()

cas_od_startu = aktualni_cas - start_Solar_Orbiter
print(cas_od_startu)

# 3 Doprava večeře (zapni hlavu)
# Zákazník si objednal večeři na webu dovážkové služby 13. listopadu 2020 v 19:47.
# Víme, že převzetí objednávky restaurací v průměru trvá 8 minut a 35 sekund, příprava jídla trvá 30 minut a doprava jídla k zákazníkovi 25 minut a 30 sekund.
# Kdy očekáváme, že jídlo dorazí zákazníkovi?

from datetime import datetime, timedelta

cas_objednavky = datetime(2022, 4, 25, 19, 47)

doba_prevzeti = timedelta(minutes=8, seconds=35)
doba_pripravy = timedelta(minutes=30)
doba_dopravy = timedelta(minutes=25, seconds=30)

cas_dodani = cas_objednavky + doba_prevzeti + doba_pripravy + doba_dopravy
cas_dodani = cas_dodani.strftime("%H:%M:%S")
print(cas_dodani)
