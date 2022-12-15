from fruitmand import fruitmand

fruitmand.append({'name': 'watermelon', 'weight': 0, 'round': True})
print(sum(x['weight'] for x in fruitmand))


