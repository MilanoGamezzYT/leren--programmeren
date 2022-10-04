a = int(input('Voer een getal in '))
b = int(input('Voer nog een getal in '))
if a > b :
    max  = a
    min = b
    print(f'a is het grootste getal {max}') 
elif a < b:
    min = a
    max = b
    print(f'a is het kleinste getal {min}')
else:
    print(f'a is gelijk aan b')

