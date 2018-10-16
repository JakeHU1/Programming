import csv

artikelnummer = ['Artikelnummer', 121, 123, 128, 137, 271]
artikelcode = ['Artikelcode', 'ABC123', 'PQR678', 'ZYX163', 'MLK709', 'TRS665']
naam = ['Naam', 'Highlight Pen', 'Nietmachine', 'Bureaulamp', 'Monitorstandaard', 'Ipad hoes']
voorraad = ['Voorraad', 231, 587, 34, 66, 155]
prijs = ['Prijs', 0.56, 9.99, 19.95, 32.50, 19.01]

with open('artikelen.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    for i in range(6):
        writer.writerow((artikelnummer[i], artikelcode[i], naam[i], voorraad[i], prijs[i]))