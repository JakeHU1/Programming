letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
i = 0
a = 0
b = 0
c = 0
while i < len(letters):
    if letters[i] == 'A':
        a += 1
        i += 1
    elif letters[i] == 'B':
        b += 1
        i += 1
    elif letters[i] == 'C':
        c += 1
        i += 1
letters2 = [a, b, c]
print(letters2)
