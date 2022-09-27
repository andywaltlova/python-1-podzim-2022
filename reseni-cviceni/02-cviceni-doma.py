# Spolubydlící (zavařovačka)
# Zkus dotáhnout náš program na finanční vypořádání spolubydlících.
# Z lekce si můžeš zkopírovat kódy, které vytvoří slovník s útratami jednotlivých spolubydlících
# a výpočet průměrné útraty na osobu.

purchase_list = [
    {"person": "Petr", "item": "Prací prášek", "value": 399},
    {"person": "Ondra", "item": "Savo", "value": 80},
    {"person": "Petr", "item": "Toaletní papír", "value": 65},
    {"person": "Libor", "item": "Pivo", "value": 124},
    {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
    {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
    {"person": "Ondra", "item": "Toaletní papír", "value": 120},
    {"person": "Míša", "item": "Pečící papír", "value": 30},
    {"person": "Zuzka", "item": "Savo", "value": 80},
    {"person": "Pavla", "item": "Máslo", "value": 50},
    {"person": "Ondra", "item": "Káva", "value": 300}
]

# Utraty jednotlivych spolubydlicich
# ! tady ta definice prazdneho slovniku chybi na kodim
sum_per_person = {}

for item in purchase_list:
    person = item["person"]
    value = item["value"]
    if person in sum_per_person:
        sum_per_person[person] += value
    else:
        sum_per_person[person] = value

# Spocitani celkove utraty
total_value = 0
for person, value in sum_per_person.items():
    total_value += value
    print(f"{person} utratil(a) za společné nákupy {value} Kč.")

# Spocitani prumerne utraty
average_value = total_value / len(sum_per_person)
print(f"Průměrná hodnota na osobu je {round(average_value)} Kč.")

# Dopiš cyklus, který projde slovník sum_per_person a pro každého ze spolubydlících vypíše,
# kolik by měl doplatit (pokud utratil(a) méně než průměr), případně kolik by měl obdržet (pokud utratil(a) více než průměr).
#  ! tady me trochu mate zadani, prijde mi ze kdyz sem utratila min nez prumer tak bych mela spis obdrzet nez doplatit
#  (zadani jsem nepsala, kazdopadne princip na reseni je stejny)

for person, utrata in sum_per_person.items():
    rozdil = round(average_value - utrata, 2)
    if rozdil > 0:
        print(f'{person} by mel obdrzet {rozdil} Kc.')
    elif rozdil < 0:
        print(f'{person} by mel doplatit {rozdil} Kc.')
        # Pripadne bez minuska
        # print(f'{person} by mel doplatit {rozdil * -1} Kc.')
    else:
        print('Jsi na 0 nemusis nic doplacet a ani nic nedostanes.')


