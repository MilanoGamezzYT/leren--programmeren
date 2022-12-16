from fruitmand import fruitmand
import random

hoeveelheid = int(input('Hoeveel fruit wil je toevoegen? '))
for x in range(hoeveelheid):
    fruit_naam = random.choice(fruitmand)
    print(fruit_naam['name'])