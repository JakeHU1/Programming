def try_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def seizoen(maand_nummer):
    maand = int(maand_nummer)
    if maand == 12 or maand == 1 or maand == 2:
        return 'winter'
    elif maand >= 3 and maand <= 5:
        return 'lente'
    elif maand >= 6 and maand <= 8:
        return 'zomer'
    elif maand >= 9 and maand <= 11:
        return 'herft'
    else:
        return 'incorrect maandnummer'
while True:
    maand = input('Geef het maandnummer: ')
    if try_int(maand) == True:
        break
    else:
        print('Voer een geldig getal in')
print(seizoen(maand))

#Lente: 3 t/m 5
#Herfst: 9 t/m 11
#Zomer: 6 t/m 8
#Winter: 12, 1, 2
