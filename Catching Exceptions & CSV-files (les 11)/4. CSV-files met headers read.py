import csv

duurtste_product = None
duurtste_product_getal = 0
kleinste_voorraad = None
kleinste_voorraad_getal = 1000000000
totaal_producten = 0
som = 0

with open('artikelen.csv', 'r') as myCSFFile:
    reader = csv.DictReader(myCSFFile, delimiter=';')
    for row in reader:
        if float(row['Prijs']) > duurtste_product_getal:
            duurtste_product_getal = float(row['Prijs'])
            duurtste_product = 'Het duurste artikel is ' + row['Naam'] + ' en die kost ' + row['Prijs'] + ' Euro'
        if int(row['Voorraad']) < kleinste_voorraad_getal:
            kleinste_voorraad_getal = int(row['Voorraad'])
            kleinste_voorraad = 'Er zijn slechts ' + row['Voorraad'] + ' exemplaren in voorraad van het product met nummer ' + row['Artikelnummer']
        som += int(row['Voorraad'])

    print('{}\n{}\nin totaal hebben wij {} producten in ons magazijn \n'.format(duurtste_product, kleinste_voorraad, som))