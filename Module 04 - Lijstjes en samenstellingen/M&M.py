import random

kleuren = ('oranje', 'blauw', 'groen', 'bruin')
hoeveelheid = int(input('hoeveel m&m zitten in de zak?'))
lijst = []
for x in range(hoeveelheid):
    random.choice(kleuren)
    lijst.append(random.choice(kleuren))
print(lijst)
