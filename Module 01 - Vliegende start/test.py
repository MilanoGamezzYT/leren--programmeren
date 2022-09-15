croissantjes = 17
croissantjesprijs = 0.39 
stokbrood = 2
stokbroodprijs = 2.78
kortingsbon = 3
kortingsprijs = 0.50
totaal = croissantjes * croissantjesprijs
totaal2 = stokbrood * stokbroodprijs
totaal3 = kortingsbon * kortingsprijs

x = int(input('Hoeveel croissantjes wilt u?  '))
totaal_croissant = x * 39
print(f'{totaal_croissant} cent')

y = int(input('Hoeveel stokbroden wilt u?    '))
totaal_stokbrood = y * 278
print(f'{totaal_stokbrood} cent')

w = int(input('Hoeveel kortingsbonnen heeft u?  '))
totaal_kortingsbonnen = w * 50

print(f'{totaal_croissant + totaal_stokbrood - totaal_kortingsbonnen} cent')