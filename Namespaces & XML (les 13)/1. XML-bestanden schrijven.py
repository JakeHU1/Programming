import xmltodict
def processXML(filename):
    with open(filename) as myXMLfile:
        filecontentstring = myXMLfile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

myXMLDict = processXML('les13.xml')
artikelnaam = myXMLDict['artikelen']['artikel']

for naam in artikelnaam:
    print(naam['naam'])