# City map of the Ultimate Mission (level 4), shown with the keyword 'city' (EN) / 'ville' (FR).
# It is a diagram, not a real map: every spot of modulesu/gamestate.py has a place on a grid
# (computed once so that 'u' = up, 'r' = right, 'd' = down, 'l' = left on the screen).
# If you add spots to gamestate.py, give them a position here too (x = column, y = row).
import pygame

SPOT_POS = {1: (11, 4), 2: (11, 3), 3: (11, 2), 4: (12, 2), 5: (13, 2), 6: (13, 5), 7: (11, 5), 8: (10, 5),
            9: (9, 5), 10: (9, 2), 11: (10, 2), 21: (14, 2), 22: (15, 2), 31: (16, 2), 32: (17, 2), 33: (18, 2),
            34: (19, 2), 35: (19, 3), 36: (19, 4), 37: (19, 5), 38: (19, 6), 39: (16, 6), 40: (16, 3),
            51: (8, 2), 52: (7, 2), 53: (6, 2), 54: (5, 2), 61: (3, 2), 62: (2, 2), 63: (2, 1), 64: (2, 0),
            65: (3, 0), 66: (3, 1), 67: (1, 0), 68: (0, 0), 71: (2, 4), 72: (3, 4), 73: (3, 5), 74: (2, 5),
            75: (2, 6), 76: (4, 5), 77: (5, 5), 78: (5, 4), 79: (5, 3), 81: (9, 6), 82: (7, 6), 83: (6, 6),
            84: (6, 7), 85: (5, 6), 86: (10, 6), 87: (10, 7), 88: (10, 8), 89: (9, 8), 90: (8, 8), 91: (7, 8)}

# Zones (same spots as modulesu/locations_coordinates.py): label EN, label FR, colour,
# and where the name is written (grid position, in an empty corner of the zone)
ZONES = [
    (list(range(1, 12)), 'Houses', 'Maisons', (255, 228, 196), (11.2, 3.5)),
    (list(range(31, 41)), 'School', 'École', (204, 229, 255), (16.4, 5.0)),
    (list(range(61, 69)), 'Shops', 'Magasins', (255, 214, 214), (0.0, 1.4)),
    (list(range(71, 80)), 'Library', 'Bibliothèque', (226, 214, 255), (-1.25, 4.6)),
    (list(range(81, 92)), 'Park', 'Parc', (205, 240, 200), (7.9, 6.8)),
    ([51, 52, 53, 54], '', '', (255, 236, 200), None),
]

# Places of interest: spot, label EN, label FR, colour, label side ('r', 'l', 'u', 'd'; 'L' = far left)
PLACES = [
    (9, 'Start', 'Départ', (40, 40, 40), 'L'),
    (32, 'School entrance', "Entrée de l'école", (40, 110, 220), 'u'),
    (36, 'Schoolyard', "Cour d'école", (40, 110, 220), 'l'),
    (21, 'Sports field', 'Terrain de sport', (60, 160, 60), 'd'),
    (4, 'Pub', 'Pub', (150, 110, 70), 'u'),  # the old stone house with a terrace (quest 11: Jack's tavern)
    (51, 'Fire station', 'Caserne', (220, 50, 40), 'u'),
    (52, 'Dollar store', 'Magasin à 1 $', (230, 140, 30), 'd'),
    (53, 'Pawn shop', 'Prêteur sur gages', (230, 140, 30), 'u'),
    (64, 'Supermarket', 'Supermarché', (220, 60, 60), 'u'),
    (66, 'Pharmacy', 'Pharmacie', (40, 170, 90), 'r'),
    (67, 'Hardware store', 'Quincaillerie', (200, 40, 40), 'd'),
    (68, 'Office store', 'Papeterie', (200, 40, 40), 'u'),
    (72, 'Library', 'Bibliothèque', (120, 90, 200), 'r'),
    (75, 'Police', 'Police', (30, 60, 160), 'r'),
    (78, 'Skatepark', 'Skatepark', (110, 110, 110), 'r'),
    (89, 'Splash pad', "Jeux d'eau", (30, 150, 220), 'd'),
    (90, 'Baseball / pirate park', 'Baseball / parc pirate', (60, 140, 60), 'l'),
]

DIR_VECT = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}  # orientation -> screen direction


def draw_city_map(surface, connections, spot, orientation, lang='en', rect=(0, 0, 1060, 575)):
    """Draw the map in rect (x, y, w, h) with the player as an arrow at 'spot' looking to 'orientation'."""
    rx, ry, rw, rh = rect
    margin_x, margin_top, margin_bottom = 70, 70, 45
    cols = max(p[0] for p in SPOT_POS.values())
    rows = max(p[1] for p in SPOT_POS.values())
    cw = (rw - 2 * margin_x) / cols
    ch = (rh - margin_top - margin_bottom) / rows

    def xy(s):
        gx, gy = SPOT_POS[s]
        return int(rx + margin_x + gx * cw), int(ry + margin_top + gy * ch)

    # background
    pygame.draw.rect(surface, (248, 244, 232), rect)
    pygame.draw.rect(surface, (90, 80, 60), rect, 3)

    font_zone = pygame.font.Font(None, 27)
    font = pygame.font.Font(None, 20)
    font_title = pygame.font.Font(None, 34)

    # zones (rounded boxes behind the streets)
    for spots, en, fr, colour, anchor in ZONES:
        pts = [xy(s) for s in spots if s in SPOT_POS]
        x0 = min(p[0] for p in pts) - 22
        x1 = max(p[0] for p in pts) + 22
        y0 = min(p[1] for p in pts) - 20
        y1 = max(p[1] for p in pts) + 20
        pygame.draw.rect(surface, colour, (x0, y0, x1 - x0, y1 - y0), border_radius=14)
    # zone names (after all boxes, so no box hides a name)
    for spots, en, fr, colour, anchor in ZONES:
        if not anchor:
            continue
        label = font_zone.render(en if lang == 'en' else fr, True, (110, 90, 60))
        ax = int(rx + margin_x + anchor[0] * cw)
        ay = int(ry + margin_top + anchor[1] * ch)
        surface.blit(label, (ax, ay - label.get_height() // 2))

    # streets
    done = set()
    for a, links in connections.items():
        for b in links.values():
            if a in SPOT_POS and b in SPOT_POS and (b, a) not in done:
                done.add((a, b))
                pygame.draw.line(surface, (150, 150, 150), xy(a), xy(b), 12)
    for a, b in done:
        pygame.draw.line(surface, (250, 250, 250), xy(a), xy(b), 4)
    for s in SPOT_POS:
        pygame.draw.circle(surface, (120, 120, 120), xy(s), 5)

    # places of interest
    for s, en, fr, colour, side in PLACES:
        x, y = xy(s)
        pygame.draw.circle(surface, colour, (x, y), 9)
        pygame.draw.circle(surface, (255, 255, 255), (x, y), 9, 2)
        text = font.render(en if lang == 'en' else fr, True, (30, 30, 30))
        w, h = text.get_size()
        pos = {'r': (x + 13, y - h // 2), 'l': (x - 13 - w, y - h // 2), 'L': (x - 28 - w, y - h // 2),
               'u': (x - w // 2, y - 14 - h), 'd': (x - w // 2, y + 13)}[side]
        bg = pygame.Surface((w + 6, h + 2), pygame.SRCALPHA)
        bg.fill((255, 255, 255, 200))
        surface.blit(bg, (pos[0] - 3, pos[1] - 1))
        surface.blit(text, pos)

    # the player: red arrow
    if spot in SPOT_POS:
        x, y = xy(spot)
        dx, dy = DIR_VECT.get(orientation, (0, -1))
        px, py = -dy, dx  # perpendicular
        tip = (x + dx * 24, y + dy * 24)
        left = (x - dx * 12 + px * 14, y - dy * 12 + py * 14)
        right = (x - dx * 12 - px * 14, y - dy * 12 - py * 14)
        pygame.draw.circle(surface, (255, 255, 255), (x, y), 22)
        pygame.draw.polygon(surface, (220, 20, 20), [tip, left, (x, y), right])
        pygame.draw.polygon(surface, (90, 0, 0), [tip, left, (x, y), right], 2)

    title = font_title.render('CITY MAP' if lang == 'en' else 'PLAN DE LA VILLE', True, (90, 70, 50))
    surface.blit(title, (rx + 16, ry + 12))
    hint = font.render('Red arrow = you (it points where you look)' if lang == 'en'
                       else 'Flèche rouge = vous (elle pointe là où vous regardez)', True, (90, 70, 50))
    surface.blit(hint, (rx + rw - hint.get_width() - 16, ry + 18))
