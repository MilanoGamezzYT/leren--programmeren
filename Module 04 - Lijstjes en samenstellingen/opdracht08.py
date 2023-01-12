from fruitmand import fruitmand
# voeg watermeloen toe aan lijst en print totale gewicht
gewicht = 0
fruitmand.append({'name': 'watermeloen', 'color': 'groen', 'weight': 0, 'round': True})

for fruit in fruitmand:
    gewicht += fruit['weight']
print(gewicht)