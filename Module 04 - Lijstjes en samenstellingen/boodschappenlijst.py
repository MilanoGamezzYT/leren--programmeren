lijstje = {}
vraag = True

while vraag:
    userInput = input('Wilt u wat toevoegen aan het boodschappenlijstje? ja/nee  ').lower()
    if userInput == 'nee' or userInput == 'n':
        vraag = False
    else:
        product_naam = str(input('Wat wil je toevoegen aan het boodschappenlijstje? ')).lower()
        hoeveelheid = int(input(f'Hoeveel wilt u toevoegen van {product_naam}? '))
        if product_naam in lijstje:
            lijstje[product_naam] += hoeveelheid
        else:
            lijstje[product_naam] = hoeveelheid

print('-[BOODSCHAPPENLIJSTJE] -')
print('')
print(lijstje)
print('')
print('---------------------')   