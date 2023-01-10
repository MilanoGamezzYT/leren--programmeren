from fruitmand import fruitmand

namen = []
kleuren = ""
gewicht = ""

for i in fruitmand:
    namen.append(i['name'])
namen.sort(key=len, reverse=True)

for i in fruitmand:
    if i['name'] == namen[0]:
        kleuren += i['color']
        gewicht += str(i['weight'])

aantal = len(namen[0])

print(f"De '{namen[0]}' ({aantal} letters) heeft een {kleuren} kleur en heeft een gewicht van {gewicht} gram")