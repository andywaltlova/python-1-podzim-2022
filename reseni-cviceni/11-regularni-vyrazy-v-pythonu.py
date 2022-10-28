# 1 Uživatelské jméno (to dáš)
# Náš systém vyžaduje od uživatele zadání uživatelského jména.
# Uživatelské jméno smí obsahovat pouze malá písmena a smí být maximálně 8 znaků dlouhé.
# Požádej uživatele o zadání uživatelského jména a pomocí regulárního výrazu vyhodnoť, zda je zadané správné.

TODO

# 2 E-mail s tečkou (to dáš)
# Uprav program na ověření e-mailu tak, aby akceptoval i e-maily, které mají v první části tečku, např. jiri.pesik@python.cz.

TODO

# 3 Záznamy (to dáš)
# Uvažujme aplikaci, která si ukládá informace o činnosti uživatelů do textového souboru. Příklad souboru je níže.

# zaznamy = """
# searchNumber: pavca.czechitas action: search phone number of user dita
# user: pavca action: send sms to phone number +420728123456
# user: jirka: action: send 2 sms to phone number +420734123456
# """

# Napiš program, který vypíše všechna telefonní čísla, která jsou v textovém souboru zmíněna.
# Nahraď tato telefonní čísla nějakým řetězcem (např. "XXX"), aby nebyla v záznamech dostupná.

TODO

# 4 Adresy stránek (zapni hlavu)
# Adresy webových stránek zpravidla začínají záhadným shlukem písmen http:// nebo https://.
# Například náš web najdete pod adresou https://kodim.cz.
# Zkrátka HTTP nebo HTTPS je ve skutečnosti označení protokolu, což je nějaký popis toho, jak by měla vypadat komunikace mezi dvěma zařízeními.
# Standardního tvaru můžeme využít, abychom z textu vytáhli všechny adresy.
# Napiš program, který z proměnné emailSRadami vytáhne všechny webové stránky, které jsou tam zmíněny.

# emailSRadami = """
# Ahoj,
# posílám ti pár tipů, kam se podívat. https://realpython.com nabízí spoustu článků i kurzů. http://docs.python.org nabízí tutoriál i rozsáhlou dokumentaci. http://www.learnpython.org nabízí hezky strukturovaný kurz pro začátečníky, rozebírá ale i nějaká pokročilejší témata. https://www.pluralsight.com je placený web, který ale kvalitou kurzů víceméně nemá konkurenci. Určitě ale sleduj i web https://www.czechitas.cz a přihlašuj se na naše kurzy!
# """

TODO

# 5 IP adresy (zapni hlavu)
# Počítačové sítě jsou ve skutečnosti postavené na číselných adresách, které jsou označeny jako IP adresy.
# Každá IP adresy je čtveřice čísel v rozsahu 0 až 255, které jsou odděleny tečkou.
# Například IP adresy webu Czechitas v internetu je 51.68.166.161.
# My ale pro zjednodušení budeme kontrolovat pouze to, zda je číslo v rozsahu 0 až 299.

# Uvažuj, že vytváříš aplikaci, která pošle testovací zprávu (tzv. ping) počítači s nějaou IP adresou.
# Napiš program, která požádá uživatele o IP adresu a zkontroluj, zda je adresa platná.
# Např. adresa 325.125.100.128 není platná (první číslo je větší než 255), adresa 152.145.146 také není platá (jde o trojici čísel, nikoli čtveřici), adresa 192.168.1.0 je platná (čtveřice čísel v daném rozsahu).

TODO

# 6 Práce s kódem (smrt v přímém přenosu)
# Chceš pomoci firmě, která vyvinula e-mailového klienta pro český trh. Níže je kousek kódu, který generuje popisky políček pro zadání adres příjemců, příjemců v kopii, příjemců ve skryté kopii a tlačítka pro odeslání nebo uložení. Nyní by firma ráda expandovala na německý trh. Bohužel vývojáři vkládali popisky do aplikace jako řetězce a ztratili přehled o řetězcích, které v aplikaci mají a které je potřeba je přeložit.

# Zkopíruj si následující kód, uložený jako řetězec, do svého programu.
# Vyhledej v programu všechny řádky, kde je ukládán řetězec do proměnné, např. řádek sender_field_title = "Příjemce".
# Pomocí dalšího regulárního výrazu vytáhni z každého řádku samotný řetězec (může být i s uvozovkami), např. "Příjemce".

# kod = """
# sender_field_title = "Příjemce"
# copy_field_title = "Kopie"
# if blind_copy == True:
#     blind_copy_title = "Skrytá kopie"
# if action == "send":
#     button_title = "Odeslat"
# else:
#     button_title = "Uložit koncept"
# """

TODO
