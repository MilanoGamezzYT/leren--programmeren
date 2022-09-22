print('Tussen welke telefoons twijfel je?')
x = input()
print('Twijfel = ' + x)
y = input()
print('en de ' + y)



prijs_iphone = int(input('Hoe duur is de iphone 13? '))
print(f'De Iphone kost €{prijs_iphone}')
prijs_samsung = int(input('Hoe duur is de Samsung? '))
print(f'De {y} kost €{prijs_samsung}')
print("")
print(f'De {x} is het duurst, de telefoon kost: €{prijs_iphone}')
print(f'De {y} is het goedkoopst, de telefoon kost: €{prijs_samsung} ')
print("")
print(f'Het advies is dus om de {x} te kopen. Deze is namelijk {prijs_iphone - prijs_samsung} euro duurder dan de {y}')








