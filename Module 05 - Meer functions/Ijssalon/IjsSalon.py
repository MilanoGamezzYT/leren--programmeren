welkom = print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.' )
aantal = int(input('Hoeveel bolletjes wilt u? '))
if aantal == 1:
    vorm = input(f'Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje?' )
    keuze = print(f'Hier is uw {vorm} met {aantal} bolletje(s).')
    meer = input('Wilt u nog meer bestellen?' )
    if meer == 'nee':
        print('Bedankt en tot ziens!')