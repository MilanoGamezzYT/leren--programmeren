from fruitmand import fruitmand

names = []
colors = ""
weight = ""

for i in fruitmand:
    names.append(i['name'])
names.sort(key=len, reverse=True)

for i in fruitmand:
    if i['name'] == names[0]:
        colors += i['color']
        weight += str(i['weight'])

aantal = len(names[0])

print(f"De '{names[0]}' ({aantal} letters) heeft een {colors} kleur en heeft een gewicht van {weight} gram")