from fruitmand import fruitmand
import random

vraag = int(input('Hoeveel fruit wil je toevoegen? '))
for x in range(vraag):
    fruit_naam = random.choice(fruitmand)
    print(fruit_naam['name'])