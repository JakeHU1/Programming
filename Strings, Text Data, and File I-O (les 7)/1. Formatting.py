def convert(celcius): #converts celsius to fahrenheit
    return celcius * 1.8 + 32

def table(fahrenheit, celcius):
    print('F \t\t C')
    i = 0
    for i in range(len(celsius)):
        print(str(fahrenheit[i]) + '\t' + str(celsius[i]))

i = 0
celsius = [-30.0, -20.0, -10.0, 0.0, 10.0, 20.0, 30.0, 40.0]
fahrenheit = []
for i in range(len(celsius)):
    fahrenheit.append(convert(celsius[i]))
table(fahrenheit, celsius)
