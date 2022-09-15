# Milan Sebes Pizza Calculator

Small = 10
Medium = 12
Large = 15


s = int(input('Hoeveel Small pizzas (25cm) (€10) wilt u hebben? '))
totaal_small = s * 10
print(f'€{totaal_small}')

m = int(input('Hoeveel Medium pizzas (29cm) (€12) wilt u hebben?  '))
totaal_medium = m * 12
print(f'€{totaal_medium}')

l = int(input('Hoeveel Large pizzas (35cm) (€15) wilt u hebben?  '))
totaal_large = l * 15
print(f'€{totaal_large}') 

print(f'€{totaal_small + totaal_medium + totaal_large} totaal')
print("Eetsmakelijk!")


