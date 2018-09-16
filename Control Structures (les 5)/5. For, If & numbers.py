getallen = [8, 10, 12, 13, 14, 15]
getallen_even =[]
i = 0
for i in range(len(getallen)):
    if getallen[i] % 2 == 0:
        getallen_even.append(getallen[i])
print(getallen_even)
