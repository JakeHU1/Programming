def som(getallenlijst):
    i, som = 0, 0
    for i in range(len(getallenlijst)):
        som += getallenlijst[i]
    return som
lijstje = [3, 5, 7, 10]
print(som(lijstje))
