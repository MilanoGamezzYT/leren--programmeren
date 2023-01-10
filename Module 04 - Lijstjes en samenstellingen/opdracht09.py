from fruitmand import fruitmand
# druif moet uit de lijst worden verwijderd
teller = 0
for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.pop(teller)
    else:
        teller += 1
        
for x in fruitmand:
    print(x['color'])



