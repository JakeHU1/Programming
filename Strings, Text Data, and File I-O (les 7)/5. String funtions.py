def gemiddelde(zin):
    aantal_characters = len(zin.replace(' ', ''))
    aantal_woorden = 0
    sorteer_woorden = zin.split(' ')
    while aantal_woorden < len(sorteer_woorden):
        aantal_woorden += 1
    return int(aantal_characters) / int(aantal_woorden)

zin = input('Voer hier de zin in waarvan u het gemiddelde van de woorden wilt berekenen: ')
print('Het gemiddelde aantal characters per woord is: ' + str(gemiddelde(zin)))
