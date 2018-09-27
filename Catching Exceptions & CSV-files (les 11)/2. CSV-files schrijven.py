from datetime import date
import time
import csv
today = date.today()
print(today)
#bestand = 'inloggers.csv'
with open('inloggers.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    while True:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        writer.writerow((((naam, voorl, gbdatum, email))))

#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file