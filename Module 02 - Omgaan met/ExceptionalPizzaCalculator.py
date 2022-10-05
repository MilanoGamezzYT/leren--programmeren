# Milan Sebes Pizza Calculator

Small = 10
Medium = 12
Large = 15

try:
    aantal_small = int(input('Hoeveel Small pizzas wilt u hebben? '))
except:
    print('dat is geen getal')
    exit()
totaal_small = aantal_small * Small
try:
    aantal_medium = int(input('Hoeveel Medium pizzas wilt u hebben?  '))
except:
        print('Dat is geen getal')
        exit()
totaal_medium = aantal_medium * Medium
try:
    aantal_large = int(input('Hoeveel Large pizzas wilt u hebben?  '))
except:
    print('Dat is geen getal')
    exit()
totaal_large = aantal_large * Large
print("")
print("--------------------------- |")
print(f'€{totaal_small} voor de {aantal_small} small pizzas  |')
print(f'€{totaal_medium} voor de {aantal_medium} medium pizzas |')
print(f'€{totaal_large} voor de {aantal_large} large pizzas  |') 
print(" ")
print(f'€{totaal_small + totaal_medium + totaal_large} totaal voor alle pizzas |')
print("Eetsmakelijk en Tot ziens!  | ")
print("--------------------------- |")