def standaardtarief(afstandKM):
    'Berekend de standaardtariefprijs van een rit'
    if afstandKM < 0:
        afstandKM = 0
    if afstandKM < 50:
        return afstandKM * 0.80
    else:
        return 15 + (afstandKM * 0.60)

def ritprijs(leeftijd, weekendrit, afstandKM):
    'Berekend de totale ritprijs op basis van de drie parameters'
    if not weekendrit and (leeftijd < 12 or leeftijd >= 65):
        return round((standaardtarief(afstandKM) * 0.7), 2)
    elif weekendrit and (leeftijd < 12 or leeftijd >= 65):
        return round((standaardtarief(afstandKM) * 0.65), 2)
    elif weekendrit and (leeftijd > 12 or leeftijd <= 65):
        return round((standaardtarief(afstandKM) * 0.6), 2)
    else:
        return round((standaardtarief(afstandKM)), 2)

while True:
    try:
        leeftijd = int(input('Geef uw leeftijd: '))
        if leeftijd <= 0:
            raise Exception
        break
    except ValueError:
        print('Voer uw leeftijd in getallen in')
    except Exception:
        print('Voer een geldige leeftijd in')

while True:
        weekendrit = input('Is deze rit in het weekend? (ja of nee) ')
        if weekendrit == 'ja' or weekendrit == 'nee':
            break
        else:
            print('Vul ja of nee in')

if weekendrit == 'ja':
    weekendrit = True
else:
    weekendrit = False

while True:
    try:
        afstandKM = int(input('Geef de afstand van uw rit: '))
        break
    except:
        print('Voer een geldige afstand in.')
print('de ritprijs bedraagt ' + str(ritprijs(leeftijd, weekendrit, afstandKM)) + ' euro')
