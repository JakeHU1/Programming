import datetime
import csv
vandaag = datetime.datetime.today()
datum = vandaag.strftime("%a %d %b %Y" + ' at ' + "%X")
#bestand = 'inloggers.csv'
with open('inloggers.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    while True:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        if voorl == 'einde':
            break
        gbdatum = input("Wat is je geboortedatum? ")
        if gbdatum == 'einde':
            break
        email = input("Wat is je e-mail adres? ")
        if email == 'einde':
            break
        writer.writerow((datum, voorl, naam, gbdatum, email))
