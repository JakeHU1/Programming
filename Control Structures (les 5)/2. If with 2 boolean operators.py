def stemmen(leeftijd, paspoort):
    if int(leeftijd) >= 18 and paspoort == 'ja':
        print('Gefeliciteerd, je mag stemmen!')
    else:
        print('Helaas, je mag nog niet stemmen.')
leeftijd = input('Geef je leeftijd: ')
paspoort = input('Nederlands paspoort: ')
stemmen(leeftijd, paspoort)
