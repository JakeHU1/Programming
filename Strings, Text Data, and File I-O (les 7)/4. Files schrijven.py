import datetime

file = open('/Users\Jake\Desktop\Hardlopers.txt', "w+")
registratie = ['Thu 10 Mar 2016, 10:45:52, Miranda', 'Thu 10 Mar 2016, 10:46:04, Piet', 'Thu 10 Mar 2016, 10:47:27, Sacha', 'Thu 10 Mar 2016, 10:48:33, Karel', 'Thu 10 Mar 2016, 10:48:42, Kemal']
for i in registratie:
    file.write(i + '\n')
file.close()

while True:
    file = open('/Users\Jake\Desktop\Hardlopers.txt', "a+")
    input('Hardloper binnen? (enter)')
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y" + ', ' + "%X, ")
    while True:
        naam = input('Wat is zijn of haar naam? ')
        try:
            test = int(naam)
            print('Geef een geldige naam')
        except ValueError:
            break
    file.write(s + naam)
    print(s + naam + ' is toegevoegd aan het bestand')
    file.close()
