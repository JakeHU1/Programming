def lang_genoeg(lengte):
    if int(lengte) >= 120:
        print('Je bent lang genoeg voor de attractie!')
    else:
        print('Sorry, je bent te klein!')
lengte = input('Geef je lengte: ')
lang_genoeg(lengte)
