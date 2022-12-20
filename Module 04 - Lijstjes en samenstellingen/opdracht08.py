from fruitmand import fruitmand

gewicht = 0
fruitmand.append({'name': 'watermelon', 'weight': 2600, })

for i in fruitmand:
    totale_gewicht = i['weight']
    gewicht += totale_gewicht
print(gewicht)
