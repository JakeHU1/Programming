def inlezen_beginstation(stations):
    'Vraagt de gebruiker wat het beginstation is. Als deze niet in traject voorkomt, foutmelding'
    while True:
        beginstation = input('Wat is je beginstation? ')
        for i in stations:
            if i.lower() == beginstation.lower():
                return beginstation.capitalize()
        print('Deze trein komt niet in ' + beginstation)

def inlezen_eindstation(stations, beginstation):
    'Vraagt de gebruiker om het eindstation. Als deze niet meer op het traject voorkomt, foutmelding'
    while True:
        eindstation = input('Wat is je eindstation? ')
        try:
            if stations.index(beginstation) < stations.index(eindstation):
                return eindstation
            elif stations.index(beginstation) == stations.index(eindstation):
                print('Daar bent u al')
            else:
                print('deze trein komt niet in ' + eindstation)
        except ValueError:
            print('Dit station komt niet voor op dit traject.')
def omroepen_reis(stations, beginstation, eindstation):
    'Toont de gebruiker de rest van de rit en waar de gebruiker uit moet stappen'
    print('{} is het {}e station in het traject'.format(beginstation, stations.index(beginstation)+1))
    #print(beginstation + ' is het ' + str(stations.index(beginstation)+1) + 'e station in het traject')
    print(eindstation + ' is het ' + str(stations.index(eindstation) + 1) + 'e station in het traject')
    print('de afstand bedraagt ' + str(int(stations.index(eindstation) - int(stations.index(beginstation)))) + ' station(s).')
    print('De prijs van het kaartje is ' + str(int(stations.index(eindstation) - int(stations.index(beginstation))) *5) + ' euro.')
    stations_over = stations[stations.index(beginstation):stations.index(eindstation)]
    del stations_over[0]
    print('jij stapt in de trein in: ' + beginstation)
    for i in stations_over:
        print('- ' + i)
    print('jij stapt uit in: ' + eindstation)


stations = ['Schagen', 'Heerhugowaart', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)