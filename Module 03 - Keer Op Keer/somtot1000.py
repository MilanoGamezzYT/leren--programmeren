nummer = 50
som = 50
letter = '50 '

while som < 1000:
    nummer += 1
    som += nummer
    letter += f' + {nummer}'
    print(f'{letter} = {som}')  