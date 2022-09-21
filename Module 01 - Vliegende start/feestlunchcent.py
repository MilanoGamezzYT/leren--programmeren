croissantjes = 17
croissantjesprijs = 39 
stokbrood = 2
stokbroodprijs = 278
kortingsbon = 3
kortingsprijs = 150
totaal = croissantjes * croissantjesprijs
totaal2 = stokbrood * stokbroodprijs
totaal3 = kortingsbon * kortingsprijs

x = int(input('Hoeveel croissantjes wilt u?  '))
totaal_croissant = x * 39
print(f'dat kost {totaal_croissant} cent')
print(" ")

y = int(input('Hoeveel stokbroden wilt u?    '))
totaal_stokbrood = y * 278
print(f'dat kost {totaal_stokbrood} cent')
print(" ")

w = int(input('Hoeveel kortingsbonnen heeft u?  '))
totaal_kortingsbonnen = w * 50
print(" ")

print(f'Dus de prijs voor de feestlunch kost {totaal_croissant + totaal_stokbrood - totaal_kortingsbonnen} cent')
print("Omgerekent is dat €10.69")