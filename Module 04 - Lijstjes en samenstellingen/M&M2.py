from random import randint

kleuren = ['bruin','rood', 'blauw','groen','geel']
hoeveelheid = int(input('Hoeveel M&M wil je hebben?'))
lijst = {}

for x in range(hoeveelheid):
    KleurVerschil = randint(0,4)
    RandomKLeur = kleuren[KleurVerschil]
    if kleuren[KleurVerschil] not in lijst:
        lijst.update({RandomKLeur : 1})
    else:
        x=lijst.get(kleuren[KleurVerschil]) +1
        lijst.update({kleuren[KleurVerschil]:x})    
print(lijst)