def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        return True
    else:
        return False
oldpassword = input('Geef oude wachtwoord: ')
newpassword = input('Geef nieuwe wachtwoord: ')
if new_password(oldpassword, newpassword) == True:
    print('nieuwe wachtwoord is aangemaakt')
else:
    print('er is iets misgegaan')
