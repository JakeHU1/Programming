import random

def monopolyworp():
    dubbel_check = 0
    while True:
        getal = [random.randint(1, 6), random.randint(1, 6)]
        #getal = [5, 5] om te testen
        if int(getal[0]) == int(getal[1]):
            dubbel_check += 1
            if dubbel_check == 3:
                print(str(getal[0]) + ' + ' + str(getal[1]) + ' = ' + str(int(getal[0]) + getal[1]) + ' (direct naar de gevangenis)')
                break
            print(str(getal[0]) + ' + ' + str(getal[1]) + ' = ' + str(int(getal[0]) + getal[1]) + ' (dubbel)')
        else:
            print(str(getal[0]) + ' + ' + str(getal[1]) + ' = ' + str(int(getal[0]) + getal[1]))
            break
monopolyworp()
