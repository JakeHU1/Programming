def try_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def toon_aantal_kluizen_vrij(): #deze funtie leest het textbestand uit en checkt hoeveel regels de textfile bevat. Vervolgens worden de beschikbare nummers uitgeprint
    file = open('/Users\Jake\Desktop\kluizen.txt', "r+")
    kluizen_vrij = 0
    lines = file.readlines()
    for line in lines:
        kluizen_vrij += 1
    print('Aantal kluizen vrij: ' + str(int(20 - kluizen_vrij)))
    file.close()

def nieuwe_kluis(): #deze funtie controleert welke kluizen vrij zijn. Vervolgens kan de klant een wachtwoord opgeven en wordt het kluisnummer toegewezen
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    file = open('/Users\Jake\Desktop\kluizen.txt', "r+")
    lines = file.readlines()
    file.close()
    for line in lines:
        regel_split = line.split(';')
        kluisnummers.remove(int(regel_split[0]))
    if kluisnummers != None:
        print('er is een kluis beschikbaar!')
        while True:
            wachtwoord = input('Geef het wachtwoord voor uw nieuwe kluis op: ')
            wachtwoord_check = input('Geef uw wachtwoord nogmaals ter controle: ')
            if wachtwoord == wachtwoord_check:
                print('Kluis ' + str(kluisnummers[0]) + ' is aan u toegewezen. U kunt deze kluis openen met uw reeds opgegeven wachtwoord.')
                break
            else:
                print('de wachtwoorden komen niet overheen, probeer het nogmaals')
    else:
        print('helaas zijn alle kluizen bezet')
    file = open('/Users\Jake\Desktop\kluizen.txt', "a+")
    file.write('\n' + str(kluisnummers[0]) + ';' + str(wachtwoord))
    file.close()

def kluis_openen():
    file = open('/Users\Jake\Desktop\kluizen.txt', "r+")
    lines = file.readlines()
    file.close()
    kluisnummer = input('Geef het kluisnummer: ')
    if kluisnummer == 'stop':
       return None
    wachtwoord = input('Geef het bijbehorende wachtwoord: ')
    for line in lines:
        regel_split = line.split('\n')
        if str(regel_split[0].replace(' ', '')) == str(kluisnummer) + ';' + str(wachtwoord):
            print('Uw kluis is succesvol geopend.')
            return None
    print('Wij hebben uw kluis niet kunnen openen met de verkregen gegevens.')

def kluis_teruggeven():
    file = open('/Users\Jake\Desktop\kluizen.txt', "r+")
    lines = file.readlines()
    file.close()
    while True:
        file = open('/Users\Jake\Desktop\kluizen.txt', "w")
        kluisnummer = input('Geef het kluisnummer: ')
        if kluisnummer == 'stop':
            for line in lines:
                file.write(line)
            break
        wachtwoord = input('Geef het bijbehorende wachtwoord: ')
        for line in lines:
            regel_split = line.split('\n')  # idee gestolen van: https://stackoverflow.com/questions/4710067/deleting-a-specific-line-in-a-file-python
            if str(regel_split[0].replace(' ', '')) != str(kluisnummer) + ';' + str(wachtwoord):
                file.write(line)
            else:
                print('Uw gegevens zijn succesvol verwijderd.')
        file.close()
        break
opties = ['1: Ik wil weten hoeveel kluizen nog vrij zijn.\n', '2: Ik wil een nieuwe kluis.\n', '3: Ik wil even iets uit mijn kluis halen.\n', '4: Ik geef mijn kluis terug.\n', '5: Ik wil stoppen.']
print(opties[0] + opties[1] + opties[2] + opties[3] + opties[4])
while True:
    keuze = input('\nWelkom in het hoofdmenu. Voer een getal in om te beginnen: ')
    if try_int(keuze) == True:
        if int(keuze) > 0 and int(keuze) <= 5:
            if keuze == '1':
                toon_aantal_kluizen_vrij()
            elif keuze == '2':
                nieuwe_kluis()
            elif keuze == '3':
                kluis_openen()
            elif keuze == '4':
                kluis_teruggeven()
            elif keuze == '5':
                print('Bedankt voor het gebruiken van mijn programma.')
                break
        else:
            print('vul een geldig getal in')
    else:
        print('vul een geldig getal in')
