def new_password(oldpassword, newpassword):
    if oldpassword == newpassword:
        return 'equal'
    elif len(newpassword) <= 6:
        return 'short'
    else:
        return True


def try_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


oldpassword = input('Geef oude wachtwoord: ')
newpassword = input('Geef nieuwe wachtwoord: ')
i = 0
while i < len(newpassword):
    if try_int(newpassword[i]) == True:
        if new_password(oldpassword, newpassword) == 'equal':
            print('Het nieuwe wachtwoord moet anders zijn dan het huidige wachtwoord')
            exit(0)
        elif new_password(oldpassword, newpassword) == 'short':
            print('Het wachtwoord moet minimaal 6 tekens lang zijn')
            exit(0)
        elif new_password(oldpassword, newpassword) == True:
            print('Het wachtwoord is succesvol verandert')
            exit(0)
    i += 1
print('Het nieuwe wachtwoord moet minimaal 1 cijfer bevatten en moet minimaal 6 tekens lang zijn')
