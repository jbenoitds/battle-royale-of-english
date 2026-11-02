# 14.06 23:10; Status: Working; Last implementations: Optimization and Modulation  

# Prev Impl Funct: Textes, Filtres transparents, Images, Accents, Sounds, Exit Code, 
# Search when ChallDisabled, Protected Spots, Xple Challenges, Addon Image, Search Evrwre Antm, 
# Special, Orientation, Image_load, Optimized, Dictionaty, Loop, Esc Trap & Search, 
# Special 3 Challenges, Random

# ONIY: (Maybe Search only on spec orientations)

import pygame
import sys
from pygame.locals import *
from modules2.voice import speak
from modules2.soundfix import load_sound
import random
from modules2.load_images import load_images
from modules2.draw_wrap_clean import draw_text, wrap_text, clean_input
from modules2.special_search import special_search
from modules2.special_shield import special_shield
from modules2.special_trap import special_trap
from modules2.phrases_extract_moyennes import moyennes_phrases
from modules2.random_dice import random_dice
from modules2.intro_screen import show_intro

def lvl2(decoy, edoc):

    ## Creations and Definitions

    # Initialize pygame
    pygame.init()

    # Dimensions of the window
    WIDTH, HEIGHT = 1060, 700
    WHITE_HEIGHT = 125  # The height of the white band at the bottom for user input

    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bataille Royale du Français")

    # Loading page (same as level 3), shown while the images load
    loader = pygame.image.load('files/loader/loader.png')
    screen.blit(loader, (0, 0))
    pygame.display.flip()

    # Variables
    num_spots = 9
    num_orientations = 4
    protec_spots = 1
    trap_spots = 2
    shield_spots = 2
    search_spots = 1

    ### Dictionary to store game states
    images = load_images(num_spots, num_orientations)
    lobby_kri = pygame.image.load('files/background/mission2/0_0.png')
    final = pygame.image.load('files/background/mission2/final.png')
    card = pygame.image.load('files/images_oth/card.png')
    shield = pygame.image.load('files/images_oth/shield.png')
    trap = pygame.image.load('files/images_oth/trap.png').convert_alpha()

    ### Dictionary to store game states
    global nextimage, all_running, search_challenge_conditions, ctrl_pressed, special_dict, quit_level
    global phrase1, phrase1g, phrase2, phrase2g, phrase3, phrase3g
    
    nextimage = lobby_kri
    all_running = True
    quit_level = False
    one = True
    k = K_1
    ff = 'full flemme'
    display_w_text = False
    input_text = ''
    ctrl_pressed = False
    text_mission = "Mission 2 : En entrant dans le Lavish Lair, la porte s'est refermée derrière vous en se verrouillant... c'était un piège pour vous emprisonner ! Objectif : trouvez la carte où est écrit le code de la porte, puis revenez à l'entrée et tapez ce code pour sortir. Mais restez sur vos gardes... Tapez 'info' puis Entrée pour voir les commandes."
    text_controls = "COMMANDES (tapez puis Entrée) : 'avant', 'gauche', 'droite', 'arrière' pour bouger. 'fouiller' pour chercher : le code de la porte est sur une carte cachée dans une pièce (désactivez d'abord pièges et boucliers). À l'entrée, tapez le code pour sortir. Défis : Ctrl + 1 pour écouter la phrase. 'quitter' pour revenir au menu, 'info' ou 'mission' pour revoir l'objectif."
    text_wrong_place = "Ce code ouvre la porte d'entrée : retournez au point de départ (l'entrée) et tapez-le là-bas."
    cmd_controls = ['info', 'commandes', 'commande', 'controles', 'contrôles', 'aide']
    cmd_mission = ['mission', 'objectif']
    cmd_quit = ['quitter', 'menu']
    help_state = {'controls': False}

    def current_text():
        return text_controls if help_state['controls'] else text_mission
    atd = 'avant'
    tag = 'gauche'
    tad = 'droite'
    fdt = 'arrière'
    w = 'w'
    a = 'a'
    d = 'd'
    s = 's'

    trap_phrases_path = 'files/texts/phrases_moy.txt'
    special_dict = moyennes_phrases(trap_phrases_path, 3)

    random_mapping = random_dice()
    dice1 = random_mapping[1] 
    dice2 = random_mapping[2]
    dice3 = random_mapping[3]

    phrase1 = special_dict[f'phrase{dice1}']
    phrase1g = f'"{phrase1}"'
    phrase2 = special_dict[f'phrase{dice2}']
    phrase2g = f'"{phrase2}"'
    phrase3 = special_dict[f'phrase{dice3}']
    phrase3g = f'"{phrase3}"'

    # Set the transparency level (alpha) for the overlay
    trap.set_alpha(130)

    # Load sounds
    pygame.mixer.init()
    sound = {
        "bus_debut_": load_sound('files/sound/mission2/bus_debut_.mp3'),
        "cheat_ff_": load_sound('files/sound/mission2/cheat_ff_.mp3'),
        "failed_chall_": load_sound('files/sound/mission2/failed_chall_.mp3'),
        "no_movement_": load_sound('files/sound/mission2/no_movement_.mp3'),
        "no_search_nnn_": load_sound('files/sound/mission2/no_search_nnn_.mp3'),
        "rotation_swoosh_": load_sound('files/sound/mission2/rotation_swoosh_.mp3'),
        "search_esc_": load_sound('files/sound/mission2/search_esc_.mp3'),
        "search_success_": load_sound('files/sound/mission2/search_success_.mp3'),
        "search_triggers_": load_sound('files/sound/mission2/search_triggers_.mp3'),
        "shield_esc_": load_sound('files/sound/mission2/shield_esc_.mp3'),
        "shield_success_": load_sound('files/sound/mission2/shield_success_.mp3'),
        "shield_triggers_": load_sound('files/sound/mission2/shield_triggers_.mp3'),
        "trap_success_": load_sound('files/sound/mission2/trap_success_.mp3'),
        "trap_triggers_": load_sound('files/sound/mission2/trap_triggers_.mp3'),
        "victory_": load_sound('files/sound/mission2/victory_.mp3'),
        "walk_": load_sound('files/sound/mission2/walk_.mp3'),
        "surprise_": load_sound('files/sound/mission2/surprise_.mp3'),
        "blipblip": load_sound('files/sound/mission2/blipblip.mp3'),
        "mipmip": load_sound('files/sound/mission2/mipmip.mp3')
    }

    # Set volume (Only for loud ones, set them lower)
    # sound["s"].set_volume(0.5)  # Set volume to 50%

    # !!! ADJUST (go in script)
    from modules2.gamestate import GameState
    game_state = GameState()


    def generate_unique_spots(num_spots, pool):
        """Generate a list of unique spots from the given pool."""
        return random.sample(pool, num_spots)

    # Initialize challenge conditions for multiple shield spots
    trap_challenge_conditions = {}
    shield_challenge_conditions = {}
    search_challenge_conditions = {}

    # Define protected spots
    protected_spots = [protec_spots]  # Spots to protect

    # Generate spots for challenges
    remaining_spots = [spot for spot in range(1, num_spots + 1) if spot not in protected_spots]

    # Traps and shields spread around the rooms (they used to end up side by side):
    # the 9 rooms make a loop (1 -> 2 -> ... -> 9 -> 1). No trap or shield right next to another one,
    # and two traps (or two shields) at least 3 rooms apart.
    def ring_distance(x, y):
        return min(abs(x - y), num_spots - abs(x - y))

    def spread_spots():
        for _ in range(2000):
            picked = random.sample(remaining_spots, trap_spots + shield_spots)
            traps, shields = picked[:trap_spots], picked[trap_spots:]
            if any(ring_distance(x, y) < 2 for i, x in enumerate(picked) for y in picked[i + 1:]):
                continue
            if any(ring_distance(x, y) < 3 for group in (traps, shields) for i, x in enumerate(group) for y in group[i + 1:]):
                continue
            return traps, shields
        picked = random.sample(remaining_spots, trap_spots + shield_spots)  # (never needed with 9 rooms)
        return picked[:trap_spots], picked[trap_spots:]

    trap_challenge_spots, shield_challenge_spots = spread_spots()
    for spot in trap_challenge_spots:
        trap_challenge_conditions[spot] = True
    for spot in shield_challenge_spots:
        shield_challenge_conditions[spot] = True
    remaining_spots = list(set(remaining_spots) - set(trap_challenge_spots) - set(shield_challenge_spots))

    # Search challenge spots
    # !!! ADJUST !!!
    search_challenge_spots = generate_unique_spots(search_spots, remaining_spots)
    for spot in search_challenge_spots:
        search_challenge_conditions[spot] = True

    ### Function to display text and images
    def display_nal(image, info_text, player_text, wrectangle):
        screen.blit(image, (0, 0))

        if game_state.spot in search_challenge_spots:
            screen.blit(card, (3 * WIDTH // 4 - card.get_width() // 2, 1 * HEIGHT // 5 - card.get_height() // 2))

        if game_state.spot in shield_challenge_spots and shield_challenge_conditions[game_state.spot]:
            screen.blit(shield, (0, 0))

        if game_state.spot in trap_challenge_spots and trap_challenge_conditions[game_state.spot]:
            screen.blit(trap, (0, 0))

        font = pygame.font.Font(None, 26)
        
        # Wrap Naruto's text
        info_lines = []
        for paragraph in info_text.split('\n'):
            info_lines.extend(wrap_text(paragraph, font, WIDTH - 20))

        for i, line in enumerate(info_lines):
            draw_text(screen, line, (10, HEIGHT - wrectangle + 34 + i * font.get_linesize()), font)

        # Wrap Player's text
        player_lines = []
        for paragraph in player_text.split('\n'):
            player_lines.extend(wrap_text(paragraph, font, WIDTH - 20))

        player_start_pos = HEIGHT - wrectangle + (len(info_lines) * font.get_linesize()) + 40
        for i, line in enumerate(player_lines):
            draw_text(screen, line, (10, player_start_pos + i * font.get_linesize()), font)

        pygame.display.flip()

    ## Main function
    def main(decoy, edoc):
        global nextimage, all_running, search_challenge_conditions, quit_level
        input_text = ''
        display_w_text = False
        one = True
        ctrl_pressed = False
        wrong_words = []

        nextimage = images[f"{game_state.spot}_{game_state.orientation}"]

        display_nal(nextimage, current_text(), "", WHITE_HEIGHT)

        while one:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        cleaned_input = clean_input(input_text)

                        if cleaned_input in cmd_controls or cleaned_input in cmd_mission:
                            if cleaned_input == 'info':  # 'info' switches between the controls and the mission
                                help_state['controls'] = not help_state['controls']
                            else:
                                help_state['controls'] = cleaned_input in cmd_controls
                            display_w_text = False
                            input_text = ''
                            display_nal(nextimage, current_text(), '', WHITE_HEIGHT)
                            continue

                        if cleaned_input in cmd_quit:
                            quit_level = True
                            all_running = False
                            return

                        if cleaned_input in [decoy, ff, edoc, atd, tag, tad, fdt, 'arriere', a, w, d, s, 'fouiller']:
                            if cleaned_input in [tad, d]:
                                sound['rotation_swoosh_'].play()
                                game_state.turn_right()

                            elif cleaned_input in [tag, a]:
                                sound['rotation_swoosh_'].play()
                                game_state.turn_left()

                            elif cleaned_input in [fdt, 'arriere', s]:
                                sound['rotation_swoosh_'].play()
                                game_state.u_turn()

                            elif cleaned_input in [atd, w]:
                                previous_spot = game_state.spot
                                previous_orientation = game_state.orientation
                                game_state.go_straight()
                                if game_state.spot == previous_spot:
                                    sound['no_movement_'].play()
                                    display_nal(nextimage, "Mouvement impossible.", '', WHITE_HEIGHT)
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == QUIT:
                                                pygame.quit()
                                                sys.exit()

                                            elif event.type == KEYDOWN:
                                                return True

                                else:
                                    sound['walk_'].play()
                            
                            elif cleaned_input == decoy:
                                sound['victory_'].play()  # the end-of-level music, as when the level is won normally...
                                sound['cheat_ff_'].play()  # ...plus "full flemme" (cheat code)
                                all_running = False
                                one = False
                                return
                            
                            elif cleaned_input == ff:
                                sound['cheat_ff_'].play()
                            
                            elif cleaned_input == edoc:
                                if game_state.spot == 1:
                                    sound['victory_'].play()
                                    all_running = False
                                    one = False
                                    return
                                else:
                                    sound['no_search_nnn_'].play()
                                    display_nal(nextimage, text_wrong_place, '', WHITE_HEIGHT)
                                    input_text = ''
                                    continue
                            
                            elif cleaned_input == 'fouiller':
                                defuse = not any(trap_challenge_conditions.values()) and not any(shield_challenge_conditions.values())
                                if game_state.spot in search_challenge_spots and defuse:
                                    if not special_search(edoc, game_state.spot, nextimage, phrase2, phrase2g, sound, display_nal, search_challenge_conditions, clean_input, decoy, WHITE_HEIGHT, k, ctrl_pressed, display_w_text):
                                        game_state.spot = game_state.spot
                                        game_state.orientation = game_state.orientation
                                    
                                    else:
                                        one = False
                                        break

                                elif game_state.spot in search_challenge_spots and not defuse:
                                    sound['no_search_nnn_'].play()
                                    display_nal(nextimage, "Vous repérez une carte dans un coin de la pièce, mais les champs d'énergie du manoir vous empêchent de l'attraper. Désactivez tous les pièges et les barrières d'énergie, puis revenez récupérer la carte.", '', WHITE_HEIGHT)
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == QUIT:
                                                pygame.quit()
                                                sys.exit()

                                            elif event.type == KEYDOWN:
                                                return True

                                else:
                                    sound['no_search_nnn_'].play()
                                    display_nal(nextimage, "Il n'y a rien à chercher ici.", '', WHITE_HEIGHT)
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == QUIT:
                                                pygame.quit()
                                                sys.exit()

                                            elif event.type == KEYDOWN:
                                                return True
                            
                            if game_state.spot in trap_challenge_spots and trap_challenge_conditions[game_state.spot]:
                                while not special_trap(game_state.spot, nextimage, phrase1, phrase1g, sound, display_nal, trap_challenge_conditions, clean_input, decoy, WHITE_HEIGHT, k, ctrl_pressed, display_w_text):
                                    pass  # Loop until the user succeeds
                                one = False
                                break
                                
                            elif game_state.spot in shield_challenge_spots and shield_challenge_conditions[game_state.spot]:
                                if not special_shield(game_state.spot, nextimage, phrase3, phrase3g, sound, display_nal, shield_challenge_conditions, clean_input, decoy, WHITE_HEIGHT, k, ctrl_pressed, display_w_text):
                                    # If failed, keep player at the same spot
                                    game_state.spot = previous_spot
                                    game_state.orientation = previous_orientation
                                    input_text = ''
                                
                                else:
                                    one = False
                                    break

                            else:
                                one = False
                                break

                        else:
                            wrong_words = []
                            sound['surprise_'].play()
                            display_w_text = True
                            input_text = ''

                    elif event.key == K_BACKSPACE:
                        input_text = input_text[:-1]

                    elif event.key in (K_LCTRL, K_RCTRL):
                        ctrl_pressed = True

                    elif event.key == pygame.K_BACKQUOTE or event.key == pygame.K_CARET:  
                        input_text = input_text
                    
                    elif ctrl_pressed and event.key == k:
                        speak(phrase1g)
                        ctrl_pressed = False

                    else:
                        input_text += event.unicode

                    if display_w_text:
                        wrong_words_str = ', '.join(wrong_words)
                        display_nal(nextimage, "Commande non reconnue. Tapez 'info' puis Entrée pour voir les commandes." + wrong_words_str, "" + input_text, WHITE_HEIGHT)
                    
                    else:
                        display_nal(nextimage, current_text(), "" + input_text, WHITE_HEIGHT)

                    pygame.display.flip()
                
                elif event.type == KEYUP and ctrl_pressed and event.key == K_q:
                    quit_level = True
                    all_running = False
                    return

                elif event.type == KEYUP and event.key in (K_LCTRL, K_RCTRL):
                    ctrl_pressed = False

    ## Intro Part

    # Start screen: picture + instructions (modules2/intro_screen.py)
    intro_title = 'MISSION 2 – Piégé dans le Lavish Lair'
    intro_lines = [
        "La porte s'est verrouillée derrière vous ! Trouvez la carte où est écrit le code de la porte, puis revenez à l'entrée (votre point de départ) et tapez le code pour sortir.",
        "- Bouger : tapez 'avant', 'gauche', 'droite' ou 'arrière', puis Entrée.",
        "- Fouiller une pièce : tapez 'fouiller' puis Entrée. La carte ne se laisse prendre que quand tous les pièges et boucliers d'énergie sont désactivés.",
        '- Pièges et boucliers : appuyez sur Ctrl + 1 pour écouter une phrase, tapez-la, puis Entrée.',
        "- Bip-bip ! = le mot que vous venez de taper est faux. Chaque fois que vous appuyez sur la barre d'espace, le jeu vérifie ce mot : corrigez-le (touche Retour arrière) avant de continuer.",
        "- Perdu ? Tapez 'info' puis Entrée à tout moment pour voir les commandes ('info' encore pour revoir la mission). 'quitter' pour revenir au menu.",
    ]
    intro_footer = 'Appuyez sur une touche pour commencer !'
    show_intro(screen, lobby_kri, intro_title, intro_lines, intro_footer, WIDTH, HEIGHT)
    sound["bus_debut_"].play()

    ## Main part

    # Main loop
    while all_running:
        main(decoy, edoc)

    if quit_level:
        return

    ## Outro part

    # Final message display
    display_nal(final, "Mission 2. Félicibravotation !!! Vous avez terminé la mission 2 de la 'Bataille Royale du Français', le premier Text-Based Game to Improve Your Writing Skills, co-developpé par Aichi Panchu et la Rascasse de l'Espace. Spéciale dédicace à PapyCat pour l'inspiration et, bien sûr, Robert le Phacochère, notre mascotte officielle. Et comme l'a bien dit notre indispensable collaborateur, ChatGPT: \"Nezourez pas le code c'est du caca !!!\"", "", WHITE_HEIGHT)

    while True:
        pygame.init()
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                return