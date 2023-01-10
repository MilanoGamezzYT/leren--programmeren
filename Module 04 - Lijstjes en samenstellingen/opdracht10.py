from fruitmand import fruitmand

lijst = sorted(fruitmand, key=lambda d: d['weight'], reverse=True)
for fruit in lijst:
    print(fruit['name'])
    print(fruit['weight'])