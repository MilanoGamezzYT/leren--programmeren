# maak de tafels van 1 t/m 10 met een functie en een input

def tafels(hoeveelheid: int):
    for getal in range(1,11):
        print(f'{getal} x {hoeveelheid} = {getal * hoeveelheid}')
while not (answer := input('Voer een getal in: ')):
    print('Voer een echt getal in')

tafels(int(answer))
        
