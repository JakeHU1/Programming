invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lijst_sort = invoer.split('-')
lijst_sort.sort()
lijst = []
i = 0
print(lijst_sort)
max = 1
min = 1
som = 0
aantal_getallen = 0
for g in lijst_sort:
    som += int(g)
    aantal_getallen += 1
    if int(g) > int(max):
        max = g
    elif int(g) < int(min):
        min = g
    else:
        continue
print('Grootste getal: ' + str(max) + ' en kleinste getal: ' + str(min))
print('Aantal getallen: ' + str(len(lijst_sort)) + ' en som van de getallen: ' + str(som))
print('Gemiddelde: ' + str(float(som / float(aantal_getallen))))
