lengte = 8
breedte = 3
diepte = 1.5

grond = lengte * breedte * diepte
print(f'{grond}')

uitgraven = 25
afvoer_grond = 32.50
totaal_uitgraven = uitgraven * grond
totaal_afvoer = afvoer_grond * grond 
offerte = totaal_afvoer + totaal_uitgraven
print(f'Offerte voor een zwembad van 8 bij 3 bij 1.5 meter, inhoud = {grond} m3')
print(f'{totaal_afvoer} + {totaal_uitgraven} = {offerte}')