naam = input('Wat is uw naam?' )
geslacht = input('Wat is uw geslacht? ')
if geslacht ==  ('man'): 
    snor1 = input('Heeft u een snor? ')
    if snor1 == 'ja':
        snor2 = int(input('Hoe breed is uw snor in cm? '))
if geslacht == ('vrouw'):
    kapsel1 = input('Wat voor kleur haar heeft u? ')
    kapsel2 = int(input('Hoelang is uw haar in cm? '))
hoge_hoed = input('Heeft u een hoge hoed? ')
rijbewijs = input('heeft u een geldig vrachtwagenbewijs?')
lengte = int(input('Hoelang bent u in cm?' ))
gewicht = int(input('Hoeveel weegt u in kg? '))
diploma = input('Heeft u een Diploma MBO-4 ondernemen?' )
certificaat = input('Heeft u een Certificaat “Overleven met gevaarlijk personeel?' )
dieren_dressuur = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?' ))
jongleren = int(input('Hoeveel jaar ervaring heeft u met jongleren?' ))
acrobatiek = int(input('Hoeveel jaar praktijkervaring heeft u met acrobatiek?' ))


if (geslacht == 'man' and snor1 == 'ja' and snor2 >= 10) or (geslacht == 'vrouw' and kapsel1 == 'rood' and kapsel2 >= 20) and hoge_hoed == 'ja' and rijbewijs == 'ja' and lengte >= 150 and gewicht >= 90 and diploma == 'ja' and certificaat == 'ja' and (dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3):
    print('Gefeliciteerd, u bent aangenomen! ')
else:
    print('U bent niet aangenomen ')

