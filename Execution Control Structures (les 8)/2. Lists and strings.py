aantal_strings = 0
vierletter_strings = []
while True:
    lijst = input("Geef lijst met minimaal 10 strings: ")
    lijst_sort = lijst.split(' ')
    while aantal_strings < len(lijst_sort):
        aantal_strings += 1
    if aantal_strings < 10:
        print('U heeft ' + str(aantal_strings) + ' strings ingevoerd, maar het minimum is 10')
    else:
        break
    break
i = 0
while i < len(lijst_sort):
    if len(lijst_sort[i]) == 4:
        vierletter_strings.append(lijst_sort[i])
        i += 1
    else:
        i += 1
print('De nieuw-gemaakte lijst met alle vier-letter strings is: ' + str(vierletter_strings))
