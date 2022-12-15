lijstje = {}
userInput = input('Wilt u wat toevoegen aan het boodschappenlijstje? ').lower()

while not userInput != 'ja':
    product_naam = str(input('Wat wilt u toevoegen aan het boodschappenlijstje? ')).lower()
    hoeveelheid = int(input(f'Hoeveel wilt u toevoegen van {product_naam}? '))
    if product_naam in lijstje:
        lijstje[product_naam] += hoeveelheid
    else:
        lijstje[product_naam] = hoeveelheid
    userInput = input('Wilt u wat toevoegen aan het boodschappenlijstje? J/N ').lower()

print('- Boodschappenlijst -')
print('')
print(lijstje)
print('')
print('------------------------')   