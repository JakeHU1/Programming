def lang_genoeg(lengte):
    if int(lengte) >= 120:
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'Sorry, je bent te klein!'
lengte = input('Geef je lengte: ')
print(lang_genoeg(lengte))
