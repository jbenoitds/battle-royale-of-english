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
    'dollar_store' : [(52, 1)],
    'daycare' : [(52, 3)],
    'pawnshop' : [(53, 1)],
    'corner_store' : [(53, 3)],
    'grocery' : [(64, 1)],
    'pharm' : [(66, 1)],
    'hardware' : [(67, 1)],
    'office' : [(68, 1)],
    'library' : [(72, 2)],
    'police' : [(75, 2)],
    'skate' : [(78, 4)],
    'watergames' : [(89, 1)],
    'baseball' : [(90, 3), (89, 3)],
    'pirateparc' : [(90, 1)],

    'friend1' : [(22, 3)],
    'friend2' : [(85, 3)],
    'friend3' : [(84, 4)],
}