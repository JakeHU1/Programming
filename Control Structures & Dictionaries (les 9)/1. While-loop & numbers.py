som, getallen = 0, 0
while True:
    getal = input('Geef een getal: ')
    if int(getal) == 0:
        print('er zijn ' + str(getallen) + ' ingevoerd, de som is: ' + str(som))
        break
    else:
        som += int(getal)
        getallen += 1