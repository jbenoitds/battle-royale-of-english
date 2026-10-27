# Zones
zones = {
    'neighbor' : list(range(1, 12)),        #11
    'school' : list(range(31, 41)),         #10
    'grocerie' : list(range(61, 69)),       #8
    'library' : list(range(71, 80)),        #9
    'parc' : list(range(81, 92)),           #11
    'else' : list(range(21, 23)) + list(range(51, 55))
}

# Locations Coordinates (so : spot_orientation)
locations = {
    'none' : [(0, 0)],
    'home' : [(1, 3)],
    'pub' : [(4, 3)],
    'foot' : [(21, 1)],
    'school' : [(32, 3)],
    'schoolyard' : [(36, 4)],
    'barber' : [(40, 4)],
    'fire' : [(51, 1)],
    'tiger' : [(52, 1)],
    'daycare' : [(52, 3)],
    'ed' : [(53, 1)],
    'dep' : [(53, 3)],
    'iga' : [(64, 1)],
    'pharm' : [(66, 1)],
    'ctire' : [(67, 1)],
    'staples' : [(68, 1)],
    'library' : [(72, 2)],
    'police' : [(75, 2)],
    'skate' : [(78, 4)],
    'watergames' : [(89, 1)],
    'baseball' : [(90, 3), (89, 3)],
    'pirateparc' : [(90, 1)],

    'ami1' : [(22, 3)],
    'ami2' : [(85, 3)],
    'ami3' : [(84, 4)],
}