def namen():
    namen = {}
    while True:
        naam = input('volgende naam: ')
        if naam == '':
            for i in namen.items():
                if i[1] == 1:
                    print('Er is ' + str(i[1]) + ' student met de naam ' + str(i[0]))
                else:
                    print('Er zijn ' + str(i[1]) + ' studenten met de naam ' + str(i[0]))
            break
        if bool(namen) == False:
            namen[naam] = 0
        for k in namen.keys():
            if k == naam:
                namen[naam] += 1
                break
            else:
                continue
        if bool(namen.get(naam)) == False:
            namen[naam] = 1

namen()


