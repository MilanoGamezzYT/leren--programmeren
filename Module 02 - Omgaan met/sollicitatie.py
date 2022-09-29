naam = input('Wat is uw naam?' )
geslacht = input('Wat is uw geslacht? ')
if geslacht ==  ('man'): 
    snor_vraag = input('Heeft u een snor? ')
    if snor_vraag == 'ja':
        snor_breedte = int(input('Hoe breed is uw snor in cm?  '))
if geslacht == ('vrouw'):
    haar_kleur = input('Wat voor kleur haar heeft u?  ')
    haar_lengte = int(input('Hoelang is uw haar in cm?  '))
hoge_hoed = input('Heeft u een hoge hoed? ')
rijbewijs = input('heeft u een geldig vrachtwagenbewijs? ')
lengte = int(input('Hoelang bent u in cm?' ))
gewicht = int(input('Hoeveel weegt u in kg? '))
diploma = input('Heeft u een Diploma MBO-4 ondernemen? ')
certificaat = input('Heeft u een certificaat genaamd Overleven met gevaarlijk personeel? ' )
dieren_dressuur = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? ' ))
jongleren = int(input('Hoeveel jaar ervaring heeft u met jongleren? ' ))
acrobatiek = int(input('Hoeveel jaar praktijkervaring heeft u met acrobatiek? ' ))
print("")

if (geslacht == 'man' and snor_vraag == 'ja' and snor_breedte >= 10) or (geslacht == 'vrouw' and haar_kleur == 'rood' and haar_lengte >= 20) and hoge_hoed == 'ja' and rijbewijs == 'ja' and lengte >= 150 and gewicht >= 90 and diploma == 'ja' and certificaat == 'ja' and (dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3):
    print(f'Gefeliciteerd {naam} u bent aangenomen!')
else:
    print('U bent niet aangenomen omdat u niet aan de eisen voldoet. ')