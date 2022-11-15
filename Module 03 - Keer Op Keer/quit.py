# stel de vraag "?" aan de gebruiker
# zolang er geen quit wordt geantwoord stel je de vraag opnieuw
# print het aantal keer dat de vraag is gesteld
x = 0
vraag = input('?  ')
while vraag != 'quit':
    vraag = input('?  ')
    x += 1
print(x)  