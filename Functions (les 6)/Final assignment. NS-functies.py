def standaardtarief(afstandKM):
    if afstandKM < 0:
        afstandKM = 0
    if afstandKM < 50:
        return afstandKM * 0.80
    else:
        return 15 + (afstandKM * 0.60)

def ritprijs(leeftijd, weekendrit, afstandKM):
    if bool(weekendrit) == False and (leeftijd < 12 or leeftijd >= 65):
        return standaardtarief(afstandKM) * 0.7
    elif bool(weekendrit) == True and (leeftijd < 12 or leeftijd >= 65):
        return standaardtarief(afstandKM) * 0.65
    elif bool(weekendrit) == True and (leeftijd > 12 or leeftijd <= 65):
        return standaardtarief(afstandKM) * 0.6
    else:
        return standaardtarief(afstandKM)

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


weekendrit = input('Is deze rit in het weekend? (ja of nee) ')

while weekendrit != "ja" and weekendrit != "nee":
        weekendrit = None
        print('vul ja of nee in')
        weekendrit = str(input('Is deze rit in het weekend? (ja of nee) '))

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
