a = int(input('Voer een getal in '))
b = int(input('Voer nog een getal in '))

if a > b: 
    print(f'a is het grootste getal: {a}')
    a = max
elif b > a:
    print(f'a is het kleinste getal: {a}')
    a = min
else:
    print('a en b zijn gelijk')

print(f'De minimum is {a}')
print(f'De maximum is {b}')
