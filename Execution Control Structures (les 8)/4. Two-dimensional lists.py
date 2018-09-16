def gemiddelde_per_student(studentencijfers):
    i = 0 #index dimensie 1
    k = 0 #index dimensie 2
    som = 0
    antw = []
    while i < int(len(studentencijfers)):
        while k < int(len(studentencijfers[i])):
            som += studentencijfers[i][k]
            k += 1
        gemiddelde = som / 3
        antw.append('student ' + str(i+1) + ' scoorde ' + str(gemiddelde) + ' gemiddeld')
        som = 0
        i += 1
        k = 0
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    i = 0
    k = 0
    aantal_cijfers = 0
    antw = 0
    while i < int(len(studentencijfers)):
        while k < int(len(studentencijfers[i])):
            antw += studentencijfers[i][k]
            k += 1
            aantal_cijfers += 1
        k = 0
        i += 1
    return antw / aantal_cijfers




studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
print(gemiddelde_per_student(studentencijfers))
print('Het gemiddelde van alle studenten is: ' + str(int(round(gemiddelde_van_alle_studenten(studentencijfers)))))
