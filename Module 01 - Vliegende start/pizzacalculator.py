# Milan Sebes Pizza Calculator

Small = 10
Medium = 12
Large = 15


s = int(input('Hoeveel Small pizzas wilt u hebben? '))
totaal_small = s * Small
print(f'€{totaal_small}')

m = int(input('Hoeveel Medium pizzas wilt u hebben?  '))
totaal_medium = m * Medium
print(f'€{totaal_medium}')

l = int(input('Hoeveel Large pizzas wilt u hebben?  '))
totaal_large = l * Large
print(f'€{totaal_large}') 

print(f'€{totaal_small + totaal_medium + totaal_large} totaal')
print("Eetsmakelijk!")


