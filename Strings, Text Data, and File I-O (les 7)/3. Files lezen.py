file = open('/Users\Jake\Desktop\Kaartnummers.txt', "r")
lines = file.readlines()
regels = 0
aantal_regels = 0
i=0
max=0

while i < len(lines):
    if lines[i] == '\n':
        regels += 1
    i += 1

for line in lines:
    regel_split = line.split(',')
    regels += 1
    if int(regel_split[0]) > int(max):
        max = regel_split[0]
        aantal_regels = regels

print('Deze file telt ' + str(regels) + ' regels')
print('Het grootste kaartnummer is: ' + str(max) + ' en dat staat op regel ' + str(aantal_regels))
file.close()
