def code(invoerstring):
    i = 0
    integers = []
    character_list = []
    word = None
    while i < len(invoerstring):
        integers.append(ord(invoerstring[i]))
        i += 1
    i = 0
    while i < len(integers):
        character_list.append(chr(int(integers[i] + 3)))
        i += 1
    word = ''.join(character_list)
    print(word)

achternaam = input('Geef uw achternaam: ')
beginstation = input('geef uw beginstation: ')
eindstation = input('Geef uw eindstation: ')
string = achternaam + beginstation + eindstation
code(string)