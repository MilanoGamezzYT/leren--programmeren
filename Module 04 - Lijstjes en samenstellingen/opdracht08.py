from fruitmand import fruitmand

gewicht = 0
fruitmand.append({'name': 'watermelon', 'weight': 2600, 'color': 'green'})

for fruit in fruitmand:
    if fruit['color'] == 'green':
        print(f'{gewicht + totale_gewicht}')
        totale_gewicht = fruit['weight']
        gewicht += totale_gewicht
else:
    print('de watermeloen is niet rood')
# print(gewicht)
