file = open('/Users\Jake\Desktop\Kaartnummers.txt', "r")
tekst = 'heeft kaartnummer: '
numbers = []
lines = file.readlines()
for line in lines:
    regel_split = line.split(',')
    print(regel_split[1].replace('\n', ' ') + tekst + regel_split[0])
file.close()
