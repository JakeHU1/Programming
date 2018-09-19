aantal_personen = input('hoeveel personen gaan er mee? ')
try:
    prijs = 4356 / int(aantal_personen)
    if prijs < 0:
        raise ValueError('Negatieve getallen zijn niet toegestaan!')
    print(prijs)
except ZeroDivisionError:
    print('Delen door 0 kan niet!')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except Exception:
    print('Onjuiste invoer!')
