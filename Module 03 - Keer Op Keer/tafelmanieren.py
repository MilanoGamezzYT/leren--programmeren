# getal = int(input('noem een getal '))

# for i in range(1,11):
#     print(f'{i} x {getal} = {i * getal}')

thislist = [5, 12, 19, 27, 3]
thislist.insert(1, 25)
print(thislist)
thislist.remove(12)

getal1 = int(input("Voer het eerste getal in"))
getal2 = int(input('Voer het tweede getal in'))

if getal1 < getal2:
    print(f'{getal1} is niet het grooste getal')
elif getal1 > getal2:
    print(f'{getal1} is het grooste getal')
else:
    print('Beide getallen zijn gelijk')


