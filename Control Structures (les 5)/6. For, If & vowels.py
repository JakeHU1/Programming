s = "Guido van Rossum heeft programmeertaal Python bedacht."
i=0
for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        print(s[i])
