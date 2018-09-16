def kwadraten_som(grondgetallen):
    i=0
    som = 0
    for i in range(len(grondgetallen)):
        if int(grondgetallen[i]) > 0:
            som += grondgetallen[i]**2
    return som

grondgetallen = [4, 5, 3, -81]
print(kwadraten_som(grondgetallen))
