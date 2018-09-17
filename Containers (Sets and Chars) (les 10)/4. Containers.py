print('test voor tuple: \n\n')

my_tuple = (1, 5, 'woord')
print(my_tuple) #dictionary is geordend, de volgorde van invoeren is bepalend

#try:
    #my_tuple[3] = 'something' --> geeft foutmelding, programma onleesbaar
#except TypeError:
    #pass
print(my_tuple) #conclusie: er is niks aan toegevoegd, dus een tuple is niet muteerbaar
print(my_tuple.__iter__()) #conclusie: een tuple is iterable, dus je kan alle values langslopen in bijvoorbeeld een for-loop
my_tuple = (1, 5, 'woord', 'woord')
print(my_tuple) #conclusie: het woord 'woord' staat er 2x in, dus dubbele waarden zijn toegestaan

print('\n')
print('test voor dictionary: \n\n')

my_dict = {'Jake': 20, 'Willem': 93}
print(my_dict) #conclusie: dictionary is geordend, de volgorde van invoeren is bepalend
my_dict['newkey'] = 'newvalue'
print(my_dict) #conclusie: conclusie: er zijn een nieuwe key en value toegevoegd, dus een dictionary is muteerbaar
print(my_dict.__iter__()) #conclusie: een dictionary is iterable, dus je kan alle values langslopen in bijvoorbeeld een for-loop door de items, keys of values
my_dict = {'Jake': 20, 'Willem': 93, 'Jake': 20}
print(my_dict)
my_dict = {'Jake': 20, 'Willem': 20}
print(my_dict) #Conclusie: de dictionary mag niet 2 keys met dezelfde value bevatten, maar de items mogen wel hetzelfde zijn

print('\n')
print('test voor set: \n\n')

my_set = set([1, 5, 7, 'word'])
print(my_set) #conclusie: een set is niet geordend, de print functie geeft de values door elkaar heen
my_set.add(8)
print(my_set)#conlusie: een nieuw element is toeevoegd aan de set, dus het is muteerbaar
print(my_set.__iter__()) #conclusie: een set is iterable, dus je kan met een loop langs alle elementen lopen
my_set.add(8)
print(my_set) #conclusie: dubble waarden zijn niet toegestaan, de 8 is niet toegevoegd

print('\n')
print('test voor list: \n\n')
my_list = [1, 5, 'word']
print(my_list) #conclusie: de list is geordend, de volgorde van invoeren is bepalend
my_list.append(8)
print(my_list) #conclusie: 8 is toegevoegd, een list is muteerbaar
print(my_list.__iter__()) #conclusie: een list is iterable, dus je kan alle values langslopen met een loop
my_list.append(8)
print(my_list) #conclusie: 8 is wederom toegevoegd, dus dubbele waarden zijn toegestaan