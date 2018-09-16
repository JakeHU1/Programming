def namen():
    namen = {}
    while True:
        naam = input('volgende naam: ')
        if naam == '':
            for i in namen.items():
                print(i)
            break
        if bool(namen) == False:
            namen[naam] = 0
        for k in namen.keys():
            print(k)
            if k == naam:
                namen[naam] += 1
                break
            else:
                continue
        if bool(namen[naam]) == False:
            namen[naam] = 0

namen()


