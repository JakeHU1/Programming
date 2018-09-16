cijferICOR = 7.0
cijferPROG = 7.5
cijferCSN = 8.0
gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3
beloning = (cijferICOR + cijferPROG + cijferCSN) * 30
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van €' + str(beloning) + ' op!'
print(overzicht)
