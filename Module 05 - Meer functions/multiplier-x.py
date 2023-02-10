# maak de tafels van 1 t/m 10 met een functie en een input

def tafels(hoeveelheid: int):
    for getal in range(1,11):
        print(f'{getal} x {hoeveelheid} = {getal * hoeveelheid}')
while True:
    getal = input('Welke tafel wil je zien? ')
    if getal == 'stop':
        break
    tafels(int(getal))
