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

km = 60
vaste_prijs = 250
prijs_per_km = 2.05
voorrijkosten = km * prijs_per_km + vaste_prijs
totaal2 = voorrijkosten  + offerte

vaste_prijs_beton = 250
meer_prijs_rood = 20
meer_prijs_keuze = 125
vierkante_meter = lengte * breedte
beton_tegels = vaste_prijs_beton * vierkante_meter
totale_prijs = totaal2 + beton_tegels
print(f'Het zwembad is {vierkante_meter} vierkante meter')
print("")
print(f'Offerte voor een zwembad van {vierkante_meter} m2 en inhoud is {grond} m3')
print(f'Uitgraven: €{totaal_uitgraven}')
print(f'Afvoeren Grond: €{totaal_afvoer}')
print(f'Voorrijkosten: €{voorrijkosten}')
print(f'Beton + Tegel voor {grond} m3: €{beton_tegels} ')
print(f'De totale prijs is: €{totaal2} + €{beton_tegels} = €{totale_prijs}')
