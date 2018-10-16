import xmltodict
def processXML(filename):
    'deze functie haalt de content uit de xml file en stopt het in een list'
    with open(filename) as myXMLfile:
        filecontentstring = myXMLfile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

myXMLDict = processXML('stations.xml')
station_lst = myXMLDict['Stations']['Station']
print('Dit zijn de codes en types van de 4 stations:')
for station in station_lst:
    print('{:4} - {}'.format(station['Code'], station['Type'])) #print de codes en types van alle stations

print('\nDit zijn alle stations met één of meer synoniemen:')
for word in station_lst:
    if word['Synoniemen'] is not None:
        print('{:4} - {}'.format(word['Code'], word['Synoniemen']['Synoniem'])) #print de stations die een of meedere synoniem(en) bevatten

print('\nDit is de lange naam van elk station:')
for lang_naam in station_lst:
    print('{:4} - {}'.format(lang_naam['Code'], lang_naam['Namen']['Lang'])) #print van ieder station de volledige naam