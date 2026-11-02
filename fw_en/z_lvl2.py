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
    pygame.display.set_caption("Battle Royale of English")

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
    ff = "so lazy"
    display_w_text = False
    input_text = ''
    ctrl_pressed = False
    text_mission = "Mission 2: As you walked into the Lavish Lair, the door slammed shut behind you and locked... it was a trap to lock you in! Goal: find the card with the door code written on it, then go back to the entrance and type the code to get out. But stay on your guard... Type 'info' then Enter to see the controls."
    text_controls = "CONTROLS (type, then Enter): 'forward', 'left', 'right', 'back' to move. 'look' to search the room: the door code is on a card hidden in one of the rooms (first disable all the traps and shields). At the entrance, type the code to get out. Challenges: Ctrl + 1 to hear the sentence. 'quit' to go back to the menu, 'info' or 'mission' to see the goal again."
    text_wrong_place = "This code opens the front door: go back to the starting point (the entrance) and type it there."
    cmd_controls = ['info', 'controls', 'control', 'commands', 'help']
    cmd_mission = ['mission', 'goal']
    cmd_quit = ['quit', 'menu']
    help_state = {'controls': False}

    def current_text():
        return text_controls if help_state['controls'] else text_mission
    atd = 'forward'
    tag = 'left'
    tad = 'right'
    fdt = 'back'
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
        
        # Wrap info text
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

                        if cleaned_input in [decoy, ff, edoc, atd, tag, tad, fdt, a, w, d, s, 'search', 'look']:
                            if cleaned_input in [tad, d]:
                                sound['rotation_swoosh_'].play()
                                game_state.turn_right()

                            elif cleaned_input in [tag, a]:
                                sound['rotation_swoosh_'].play()
                                game_state.turn_left()

                            elif cleaned_input in [fdt, s]:
                                sound['rotation_swoosh_'].play()
                                game_state.u_turn()

                            elif cleaned_input in [atd, w]:
                                previous_spot = game_state.spot
                                previous_orientation = game_state.orientation
                                game_state.go_straight()
                                if game_state.spot == previous_spot:
                                    sound['no_movement_'].play()
                                    display_nal(nextimage, "Can't move that way.", '', WHITE_HEIGHT)
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
                            
                            elif cleaned_input in ('look', 'search'):
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
                                    display_nal(nextimage, "You spot a card in a corner of the room, but the mansion's energy fields stop you from grabbing it. Disable all the traps and energy barriers, then come back for the card.", '', WHITE_HEIGHT)
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == QUIT:
                                                pygame.quit()
                                                sys.exit()

                                            elif event.type == KEYDOWN:
                                                return True

                                else:
                                    sound['no_search_nnn_'].play()
                                    display_nal(nextimage, "There's nothing to search here.", '', WHITE_HEIGHT)
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
                        display_nal(nextimage, "Unknown command. Type 'info' then Enter to see the controls." + wrong_words_str, "" + input_text, WHITE_HEIGHT)
                    
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
    intro_title = 'MISSION 2 – Trapped in the Lavish Lair'
    intro_lines = [
        'The door locked behind you! Find the card with the door code, then go back to the entrance (where you start) and type the code to get out.',
        "- Move: type 'forward', 'left', 'right' or 'back', then press Enter.",
        "- Search a room: type 'look' then Enter. The card only lets itself be taken once every trap and energy shield is disabled.",
        '- Traps and shields: press Ctrl + 1 to hear a sentence, type it, then press Enter.',
        '- Bip-bip! = the word you just typed is wrong. Each time you press the space bar, the game checks that word: fix it (Backspace) before going on.',
        "- Lost? Type 'info' then Enter at any time to see the controls ('info' again shows the mission). 'quit' goes back to the menu.",
    ]
    intro_footer = 'Press any key to start!'
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
    display_nal(final, "Mission 2. Congratu-bravo-lations !!! You have finished mission 2 of the 'Battle Royale of English', the first Text-Based Game to Improve Your Writing Skills, co-developed by Aichi Panchu and the Space Scorpionfish. Special shout-out to PapyCat for the inspiration and, of course, Robert the Warthog, our official mascot. And as our essential collaborator ChatGPT so wisely said: \"Don't look at the code, it's a mess !!!\"", "", WHITE_HEIGHT)

    while True:
        pygame.init()
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                return