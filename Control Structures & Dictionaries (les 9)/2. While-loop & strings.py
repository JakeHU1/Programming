while True:
    woord = input('Geef een string van vier letters: ')
    if len(woord) == 4:
        print('Inlezen van correcte string: ' + woord + ' is geslaagd')
        break
    #elif len(woord) == 0:
        #print('Vul een woord in')
    else:
        print(woord + ' heeft ' + str(len(woord)) + ' letters')