# Status: W:  
# Last:
# Next: Faire un menu avec les 3 niveaux
# Next: 4th Wall
# Next: Persos qui flottent (devraient etre fixés par leur limite du bas, pas leur moitié,
# Next: et l'image devrait avoir une surface de sol a la moitié, ou l'on place perso)
# Maintenance: Documentation
# M: Fenêtre extensibles
# M: fichiers son des dict 4, 5, 6 et 7 tous id. régler ça ici et dans scripts son 
# Optional: (High scores: pas motivé, pas oblig.)

import sys
import pygame
from pygame.locals import *
import random
from modules3.load_images_mov import load_images_mov
from modules3.draw_wrap_clean import draw_text, wrap_text, clean_input
from modules3.special_search import special_search
from modules3.special_shield import special_shield
from modules3.special_trap import special_trap
from modules3.special_enemy import special_enemy
from modules3.load_sounds import load_sounds
from modules3.load_images_oth import ImageLoader
from modules3.phrases_extract_other import other_phrases
from modules3.phrases_extract_moyennes import moyennes_phrases
from modules3.load_images_enemy import ImageLoaderEnemy
from modules3.load_sounds_enemy import load_sounds_enemy
from modules3.random_dice import random_dice
from modules3.intro_screen import show_intro

def lvl3(decoy, edoc):

    ## Creations and Definitions

    ### Window
    # Initialize pygame
    pygame.init()

    # Dimensions of the window
    WIDTH, HEIGHT = 1060, 700
    WHITE_HEIGHT = 125  # The height of the white band at the bottom for user input

    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bataille Royale du Français")

    loader = pygame.image.load('files/loader/loader.png')
    screen.blit(loader,(0,0))
    pygame.display.flip()

    # Find the path to text
    enemy_phrase_gde_path = 'files/texts/phrases_gde.txt'
    enemy_phrase_moy_path = 'files/texts/phrases_moy.txt'
    enemy_phrase_pet_path = 'files/texts/phrases_pet.txt'

    ### Variables
    # !!! ADJUST
    global nextimage, all_running, search_challenge_conditions, enemy, counter1, counterk
    global kakachi_gang_trigger, key_trigger, user_lives, enemy_lives, enemy, counter1, counterk 
    global enemy_alive, enemy_spots, random_mapping, kakachi_gang_trigger, key_trigger, quit_level
    number_levels = 3
    level = 0

    user_lives = 4
    enemy_lives = 3 # careful, they're redifined = x in main
    enemy_alive = 1 # samesies

    enemy = 1
    counter1 = 0
    counterk = 3

    protected_spots = [1]  # Spots to protect

    num_spots = 25
    num_orientations = 4
    trap_spots = 0
    shield_spots = 0
    search_spots = 1

    enemy_spots = 3
    kakachi_gang_spots = 3

    num_phr_per = enemy_spots

    # 3 pour special, 1 pour kakachi
    num_phr_tot_moy = 3 + 3 * enemy_spots + 3 * kakachi_gang_spots + 3
    num_phr_tot_gde = num_phr_tot_pet = 3 * enemy_spots + 3 * kakachi_gang_spots + 3

    phrase_dict_moy1, phrase_dict_moy2, phrase_dict_moy3, phrase_dict_moy4, phrase_dict_moy5, phrase_dict_moy6, phrase_dict_moy_kakachi, special_dict = moyennes_phrases(enemy_phrase_moy_path, num_phr_tot_moy, num_phr_per)
    phrase_dict_gde1, phrase_dict_gde2, phrase_dict_gde3, phrase_dict_gde4, phrase_dict_gde5, phrase_dict_gde6, phrase_dict_gde_kakachi = other_phrases(enemy_phrase_gde_path, num_phr_tot_gde, num_phr_per)
    phrase_dict_pet1, phrase_dict_pet2, phrase_dict_pet3, phrase_dict_pet4, phrase_dict_pet5, phrase_dict_pet6, phrase_dict_pet_kakachi = other_phrases(enemy_phrase_pet_path, num_phr_tot_pet, num_phr_per)

    phrase_dicts_gde = phrase_dict_gde1, phrase_dict_gde2, phrase_dict_gde3, phrase_dict_gde4, phrase_dict_gde5, phrase_dict_gde6
    phrase_dicts_moy = phrase_dict_moy1, phrase_dict_moy2, phrase_dict_moy3, phrase_dict_moy4, phrase_dict_moy5, phrase_dict_moy6
    phrase_dicts_pet = phrase_dict_pet1, phrase_dict_pet2, phrase_dict_pet3, phrase_dict_pet4, phrase_dict_pet5, phrase_dict_pet6

    enemy_text = {
        0: "Devant vous se dresse Dark Va Dehors, qui est très méchant quand il ne peut pas aller dehors, et là il est dedans! \nÉcoutez une phrase avec \"Ctrl + 1\", \"Ctrl + 2\" ou \"Ctrl + 3\", puis tapez-la pour lui enlever des vies. Commencez par \"1.\" pour utiliser le pistolet (-1 vie, 2 balles), \"2.\" pour la mitraillette (-2 vies, 100 balles) et \"3.\" pour le shotgun (-3 vies, 1 cartouche).",
        1: "Devant vous se dresse Mario, it's lui, Mario. Armé de sa clé à molette de plombier, il a pas l'air commode! \nÉcoutez une phrase avec \"Ctrl + 1\", \"Ctrl + 2\" ou \"Ctrl + 3\", puis tapez-la pour lui enlever des vies. Commencez par \"1.\" pour utiliser le pistolet (-1 vie, 2 balles), \"2.\" pour la mitraillette (-2 vies, 100 balles) et \"3.\" pour le shotgun (-3 vies, 1 cartouche).",
        2: "Devant vous se dresse Sacha et Pikachu, cruels et qui puent des pieds. Des dévoreurs de combattants de la Bataille Royale ! \nÉcoutez une phrase avec \"Ctrl + 1\", \"Ctrl + 2\" ou \"Ctrl + 3\", puis tapez-la pour leur enlever des vies. Commencez par \"1.\" pour utiliser le pistolet (-1 vie, 2 balles), \"2.\" pour la mitraillette (-2 vies, 100 balles) et \"3.\" pour le shotgun (-3 vies, 1 cartouche).",
        3: "Voilà Naruto, le premier à venir venger Kakachi et peut-être même récupérer son Nuka-Cola! \nÉcoutez une phrase avec \"Ctrl + 1\", \"Ctrl + 2\" ou \"Ctrl + 3\", puis tapez-la pour leur enlever des vies. Commencez par \"1.\" pour utiliser le pistolet (-1 vie, 2 balles), \"2.\" pour la mitraillette (-2 vies, 100 balles) et \"3.\" pour le shotgun (-3 vies, 1 cartouche).",
        4: "Et c'est au tour de Sasuke de se joindre au combat, arriverez-vous a le mettre K.O. ? \nÉcoutez une phrase avec \"Ctrl + 1\", \"Ctrl + 2\" ou \"Ctrl + 3\", puis tapez-la pour leur enlever des vies. Commencez par \"1.\" pour utiliser le pistolet (-1 vie, 2 balles), \"2.\" pour la mitraillette (-2 vies, 100 balles) et \"3.\" pour le shotgun (-3 vies, 1 cartouche).",
        5: "C'est Sakura à présent qui arrive en courant pour tenter de vous battre, mais y arrivera-t-elle? \nÉcoutez une phrase avec \"Ctrl + 1\", \"Ctrl + 2\" ou \"Ctrl + 3\", puis tapez-la pour leur enlever des vies. Commencez par \"1.\" pour utiliser le pistolet (-1 vie, 2 balles), \"2.\" pour la mitraillette (-2 vies, 100 balles) et \"3.\" pour le shotgun (-3 vies, 1 cartouche)."
    }

    kakachi_text = "Hmmmm, le Nuka Cola, si rafraîchissant! Kakachi en a et il vous nargue, mais vous n'avez pas dit votre dernier mot. \nÉcoutez une phrase avec \"Ctrl + 1\", \"Ctrl + 2\" ou \"Ctrl + 3\", puis tapez-la pour leur enlever des vies. Commencez par \"1.\" pour utiliser le pistolet (-1 vie, 2 balles), \"2.\" pour la mitraillette (-2 vies, 100 balles) et \"3.\" pour le shotgun (-3 vies, 1 cartouche)."

    random_mapping = random_dice()


    ### Load images
    # !!! ADJUST (mov: dans script load_images_mov)
    images = load_images_mov(num_spots, num_orientations)

    # !!! ADJUST (mov: dans script load_images_oth)
    folder_path = 'files/images_oth'
    enemy_folder_path = 'files/images_enemy'
    load = ImageLoader(folder_path)
    load_enemy = ImageLoaderEnemy(enemy_folder_path)

    # Define paths to the image and sound folders
    image_folder = 'files/images_enemy'
    sound_folder = 'files/sound_enemy'

    sound_dict1, sound_dict2, sound_dict3, sound_dict4, sound_dict5, sound_dict6, sound_dict7 = load_sounds_enemy(sound_folder)
    sound_dicts = [sound_dict1, sound_dict2, sound_dict3, sound_dict4, sound_dict5, sound_dict6]

    # Set the transparency level (alpha) for the overlay
    load.get('trap').set_alpha(130)


    ### Dictionary to store game states
    nextimage = load.get('lobby')
    all_running = True
    quit_level = False
    one = True
    k = K_1
    ff = 'full flemme'
    display_w_text = False
    display_f_text = False
    display_s_text = False
    input_text = ''
    ctrl_pressed = False
    text_all = "Mission 3 : En sortant du Lavish Lair, vous réalisez que vous n'avez pas les clés de la voiture (sûrement à la bibliothèque) et, avec cette chaleur, vous boiriez bien un Nuka-Cola bien frais (il devrait y en avoir aux cuisines).\nObjectifs restants : - Nuka-Cola ; - Clés ; - Taper le code des clés à l'entrée. Tapez 'info' pour voir les commandes."
    text_key = "Mission 3 : En sortant du Lavish Lair, vous réalisez que vous n'avez pas les clés de la voiture (sûrement à la bibliothèque) et, avec cette chaleur, vous boiriez bien un Nuka-Cola bien frais (il devrait y en avoir aux cuisines).\nObjectifs restants : - Nuka-Cola ; - Taper le code des clés à l'entrée. Tapez 'info' pour voir les commandes."
    text_cola = "Mission 3 : En sortant du Lavish Lair, vous réalisez que vous n'avez pas les clés de la voiture (sûrement à la bibliothèque) et, avec cette chaleur, vous boiriez bien un Nuka-Cola bien frais (il devrait y en avoir aux cuisines).\nObjectifs restants : - Clés ; - Taper le code des clés à l'entrée. Tapez 'info' pour voir les commandes."
    text_finish = "Mission 3 : En sortant du Lavish Lair, vous réalisez que vous n'avez pas les clés de la voiture (sûrement à la bibliothèque) et, avec cette chaleur, vous boiriez bien un Nuka-Cola bien frais (il devrait y en avoir aux cuisines).\nObjectif restant : - Taper le code des clés à l'entrée. Tapez 'info' pour voir les commandes."
    text_controls = "COMMANDES (tapez puis Entrée) : 'avant', 'gauche', 'droite', 'arrière' pour bouger. 'fouiller' pour chercher les clés. Combats : Ctrl + 1, 2 ou 3 pour écouter une phrase, puis tapez '1.', '2.' ou '3.' suivi de la phrase. À la fin, tapez le code des clés à l'entrée (le point de départ). 'quitter' pour revenir au menu, 'info' ou 'mission' pour revoir les objectifs."
    text_wrong_place = "Ce code fait biper la voiture, qui est garée devant l'entrée : retournez au point de départ et tapez-le là-bas."
    text_no_keys = "Ce code va avec les clés de la voiture... que vous n'avez pas encore ! Allez d'abord les chercher (sûrement à la bibliothèque)."
    cmd_controls = ['info', 'commandes', 'commande', 'controles', 'contrôles', 'aide']
    cmd_mission = ['mission', 'objectif', 'objectifs']
    cmd_quit = ['quitter', 'menu']
    help_state = {'controls': False}
    # Movement: full words (shown to the player) + secret one-letter shortcuts w/a/s/d
    mv_forward = ['avant', 'w']
    mv_left = ['gauche', 'a']
    mv_right = ['droite', 'd']
    mv_back = ['arrière', 'arriere', 's']
    a = 'a'
    w = 'w'
    d = 'd'
    s = 's'


    ### Load sounds
    # !!! ADJUST (go in script)
    pygame.mixer.init()
    folder_path = 'files/sound/mission3'
    sound = load_sounds(folder_path)

    # Set volume (Only for loud ones, set them lower)
    # sound["s"].set_volume(0.5)  # Set volume to 50%


    ### GameState
    # !!! ADJUST (go in script)
    from modules3.gamestate import GameState
    game_state = GameState()


    ### Randomization and Specials
    def generate_unique_spots(num_spots, pool):
        """Generate a list of unique spots from the given pool."""
        return random.sample(pool, num_spots)

    # Initialize challenge conditions for multiple shield spots
    trap_challenge_conditions = {}
    shield_challenge_conditions = {}
    search_challenge_conditions = {}
    enemy_challenge_conditions = {}
    kakachi_gang_challenge_conditions = {}
    kakachi_challenge_conditions = {}

    # Generate spots for challenges within specified ranges
    # !!! ADJUST
    trap_pool = list(range(1, 10))
    shield_pool = list(range(1, 10))

    # !!! ADJUST
    search_pool = list(range(24, 26))
    enemy_pool = list(range(21, 24)) + list(range(3, 7))

    # remove comment when: 1. enough phrases; 2. a refreshing mission there
    #enemy_pool = list(range(10, 15)) + list(range(21, 26))

    # Function to generate unique spot_orientation combinations from a custom pool
    def generate_unique_spot_orientations(num_combinations, pool, num_orientations, game_state):
        spot_orientations = []
        for _ in range(num_combinations):
            while True:
                spot = random.choice(pool)
                orientation = random.randint(1, num_orientations)
                game_state.spot = spot
                game_state.orientation = orientation
                next_spot = game_state.can_go_forward()
                if next_spot:
                    spot_orientations.append((spot, orientation))
                    pool.remove(spot)
                    break
        return spot_orientations

    # Remove protected spots from pools
    trap_pool = [spot for spot in trap_pool if spot not in protected_spots]
    shield_pool = [spot for spot in shield_pool if spot not in protected_spots]
    search_pool = [spot for spot in search_pool if spot not in protected_spots]
    enemy_pool = [spot for spot in enemy_pool if spot not in protected_spots]

    # Make a copy of the initial pools to track used spots
    used_spots = set()

    # Trap challenge spots
    trap_challenge_spots = generate_unique_spots(trap_spots, trap_pool)
    for spot in trap_challenge_spots:
        trap_challenge_conditions[spot] = True
        used_spots.add(spot)

    # Shield challenge spots
    available_shield_pool = [spot for spot in shield_pool if spot not in used_spots]
    shield_challenge_spots = generate_unique_spots(shield_spots, available_shield_pool)
    for spot in shield_challenge_spots:
        shield_challenge_conditions[spot] = True
        used_spots.add(spot)

    # Search challenge spots
    available_search_pool = [spot for spot in search_pool if spot not in used_spots]
    search_challenge_spots = generate_unique_spots(search_spots, available_search_pool)
    for spot in search_challenge_spots:
        search_challenge_conditions[spot] = True
        used_spots.add(spot)

    # Enemy challenge spots
    enemy_spots_orientations = generate_unique_spot_orientations(enemy_spots, enemy_pool, num_orientations, game_state)
    # Kakachi's gang (after Kakachi): two on the way out, the second one waits in the cellar next to the kitchen
    kakachi_gang_spots_orientations = [(11, 4), (15, 1), (13, 4),]
    kakachi_spot_orientation = [(14, 3)]

    kakachi_gang_trigger = False
    key_trigger = False

    # Store enemy spot orientations in a dictionary
    for spot, orientation in enemy_spots_orientations:
        enemy_challenge_conditions[(spot, orientation)] = True  # Initially set to True or False based on game logic

    for spot, orientation in kakachi_gang_spots_orientations:
        kakachi_gang_challenge_conditions[(spot, orientation)] = True  # Initially set to True or False based on game logic

    kakachi_challenge_conditions[(14, 3)] = True

    ### display_nal: Function to display text and images
    def display_nal(image, info_text, player_text, wrectangle, enemy_lives, user_lives, enemy, enemy_alive):
        if enemy_lives < 0:
            enemy_lives = 0
        
        elives_str = f'elives{enemy_lives}'
        ulives_str = f'ulives{user_lives}'

        if enemy_lives > 0:
            enemy_alive = 1
        else:
            enemy_alive = 0
        enemy_str = f'{enemy}{enemy_alive}'
        
        screen.blit(image, (0, 0))

        if image != load.get('lobby'):
            screen.blit(load.get(ulives_str), (40, 515))

        if game_state.spot in search_challenge_spots:
            screen.blit(load.get('carkeys'), (4 * WIDTH // 5 - load.get('carkeys').get_width() // 2, 3 * HEIGHT // 5 - load.get('carkeys').get_height() // 2))

        elif game_state.spot in shield_challenge_spots and shield_challenge_conditions[game_state.spot]:
            screen.blit(load.get('shield'), (0, 0))

        elif game_state.spot in trap_challenge_spots and trap_challenge_conditions[game_state.spot]:
            screen.blit(load.get('trap'), (0, 0))

        elif (game_state.spot, game_state.orientation) in enemy_challenge_conditions and enemy_challenge_conditions[(game_state.spot, game_state.orientation)]:
            # !!! Adjust position hearts with respect to image, not absolute, and find correct
            screen.blit(load.get(elives_str), (1 * WIDTH // 2 - load.get(elives_str).get_width() // 2, 2 * HEIGHT // 5 - load_enemy.get_enemy(enemy_str).get_height() // 2 - load.get(elives_str).get_height()))
            screen.blit(load_enemy.get_enemy(enemy_str), (1 * WIDTH // 2 - load_enemy.get_enemy(enemy_str).get_width() // 2, 2 * HEIGHT // 5 - load_enemy.get_enemy(enemy_str).get_height() // 2))

        elif (game_state.spot, game_state.orientation) in kakachi_gang_challenge_conditions and kakachi_gang_challenge_conditions[(game_state.spot, game_state.orientation)] and kakachi_gang_trigger:
            # !!! Adjust position hearts with respect to image, not absolute, and find correct
            screen.blit(load.get(elives_str), (1 * WIDTH // 2 - load.get(elives_str).get_width() // 2, 2 * HEIGHT // 5 - load_enemy.get_enemy(enemy_str).get_height() // 2 - load.get(elives_str).get_height()))
            screen.blit(load_enemy.get_enemy(enemy_str), (1 * WIDTH // 2 - load_enemy.get_enemy(enemy_str).get_width() // 2, 2 * HEIGHT // 5 - load_enemy.get_enemy(enemy_str).get_height() // 2))
        
        elif (game_state.spot, game_state.orientation) in kakachi_challenge_conditions and kakachi_challenge_conditions[(game_state.spot, game_state.orientation)]:
            # !!! Adjust position hearts with respect to image, not absolute, and find correct
            screen.blit(load.get(elives_str), (1 * WIDTH // 2 - load.get(elives_str).get_width() // 2, 2 * HEIGHT // 5 - load_enemy.get_enemy(enemy_str).get_height() // 2 - load.get(elives_str).get_height()))
            screen.blit(load_enemy.get_enemy(enemy_str), (1 * WIDTH // 2 - load_enemy.get_enemy(enemy_str).get_width() // 2, 2 * HEIGHT // 5 - load_enemy.get_enemy(enemy_str).get_height() // 2))

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

    # !!! ADJUST
    # Set starting position (adjust as per your game's requirement)
    game_state = GameState(spot=1, orientation=3)

    # Initialize pygame and other necessary components
    pygame.init()


    ## Main function
    def main(decoy, edoc):
        global nextimage, all_running, search_challenge_conditions, enemy, counter1, counterk, kakachi_gang_trigger, key_trigger, quit_level
        input_text = ''
        display_w_text = False
        display_f_text = False
        display_s_text = False
        one = True
        ctrl_pressed = False
        wrong_words = []

        user_lives = 4
        enemy_lives = 3

        if kakachi_gang_trigger:
            if key_trigger:
                text = text_finish
            else:
                text = text_cola
        elif key_trigger:
            text = text_key
        else:
            text = text_all

        if help_state['controls']:
            text = text_controls

        nextimage = images[f"{game_state.spot}_{game_state.orientation}"]
        display_nal(nextimage, text, "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

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
                            one = False
                            break  # main() is called again and shows the right text

                        if cleaned_input in cmd_quit:
                            quit_level = True
                            all_running = False
                            return

                        if cleaned_input in [decoy, ff, edoc, 'fouiller'] + mv_forward + mv_left + mv_right + mv_back:
                            if cleaned_input in mv_right:
                                sound['rotation_swoosh_'].play()
                                game_state.turn_right()
                                nextimage = images[f"{game_state.spot}_{game_state.orientation}"]

                            elif cleaned_input in mv_left:
                                sound['rotation_swoosh_'].play()
                                game_state.turn_left()
                                nextimage = images[f"{game_state.spot}_{game_state.orientation}"]

                            elif cleaned_input in mv_back:
                                sound['rotation_swoosh_'].play()
                                game_state.u_turn()
                                nextimage = images[f"{game_state.spot}_{game_state.orientation}"]

                            elif cleaned_input in mv_forward:
                                previous_spot = game_state.spot
                                previous_orientation = game_state.orientation
                                game_state.go_straight()
                                if not (game_state.spot in shield_challenge_spots and shield_challenge_conditions[game_state.spot]):
                                    nextimage = images[f"{game_state.spot}_{game_state.orientation}"]

                                if game_state.spot == previous_spot:
                                    sound['no_movement_'].play()
                                    display_nal(nextimage, "Mouvement impossible.", '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue  # Keep capturing key events for the next command

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
                                if game_state.spot == 1 and not key_trigger:
                                    sound['no_search_nnn_'].play()
                                    display_nal(nextimage, text_no_keys, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue
                                elif game_state.spot == 1:
                                    if kakachi_gang_trigger:
                                        sound['victory_'].play()
                                        all_running = False
                                        one = False
                                        return
                                    else:
                                        sound['no_search_nnn_'].play()
                                        display_nal(nextimage, "Vous avez la clé et, en appuyant sur le bouton, vous entendez et repérez la voiture au loin, mais il fait si chaud... trop chaud pour s'aventurer dehors sans avoir d'abord dégusté un succulent Nuka-Cola! Allez voir aux cuisines, si vous en trouvez.", '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                        input_text = ''
                                        continue
                                else:
                                    sound['no_search_nnn_'].play()
                                    display_nal(nextimage, text_wrong_place, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue

                            elif cleaned_input == 'fouiller':
                                # !!! Adjust, commenté pour mission 3, pas besoin
                                #defuse = not any(trap_challenge_conditions.values()) and not any(shield_challenge_conditions.values())
                                # !!! Adjust, commenté pour mission 3, pas besoin
                                if game_state.spot in search_challenge_spots: #and defuse:
                                    # !!! ADJUST (give phrase x to this challenge)
                                    if not special_search(edoc, game_state.spot, nextimage, special_dict['phrase2'], sound, display_nal, search_challenge_conditions, clean_input, decoy, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive, k, ctrl_pressed, display_w_text):
                                        game_state.spot = game_state.spot
                                        game_state.orientation = game_state.orientation
                                    
                                    else:
                                        key_trigger = True
                                        one = False
                                        break
                                
                                # !!! Adjust, commenté pour mission 3, pas besoin
                                #elif game_state.spot in search_challenge_spots and not defuse:
                                #    sound['no_search_nnn_'].play()
                                #    display_nal(nextimage, "Vous repérez les clés dans un coin de la pièce, mais les champs d'énergie du manoir vous empêchent de l'attraper (encore?! Il s'est pas foulé l'auteur!). Désactivez les pièges et les barrières d'énergie, puis revenez récupérer les clés.", '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                #    input_text = ''
                                #    continue
                                                                
                                else:
                                    sound['no_search_nnn_'].play()
                                    display_nal(nextimage, "Il n'y a rien à chercher ici.", '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue
                                                        
                            if game_state.spot in trap_challenge_spots and trap_challenge_conditions[game_state.spot]:
                                # !!! ADJUST (give phrase x to this challenge)
                                while not special_trap(game_state.spot, nextimage, special_dict['phrase1'], sound, display_nal, trap_challenge_conditions, clean_input, decoy, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive, k, ctrl_pressed, display_w_text):
                                    pass  # Loop until the user succeeds
                                one = False
                                break

                            elif (game_state.spot, game_state.orientation) in enemy_challenge_conditions and enemy_challenge_conditions[(game_state.spot, game_state.orientation)]:
                                if counter1 < enemy_spots:

                                    # Dice dict

                                    counter1_dice = random_mapping[counter1]
                                    enemy = counter1_dice + 1

                                    phrase_dict_gde = phrase_dicts_gde[counter1_dice]
                                    phrase_dict_moy = phrase_dicts_moy[counter1_dice]
                                    phrase_dict_pet = phrase_dicts_pet[counter1_dice]
                                    sound_dict = sound_dicts[counter1_dice]
                                    etext = enemy_text[counter1_dice]

                                    # Loop until the user succeeds
                                    while not special_enemy(
                                        decoy, etext, user_lives, enemy_lives, enemy, enemy_alive, game_state.spot, game_state.orientation,
                                        nextimage, phrase_dict_gde, phrase_dict_moy, phrase_dict_pet, sound_dict, sound,
                                        display_nal, enemy_challenge_conditions, clean_input, WHITE_HEIGHT,
                                        k, ctrl_pressed, display_f_text, display_s_text
                                    ):
                                        pass  # Loop until the user succeeds
                                    
                                    counter1 = counter1 + 1
                                    one = False  # Exit the loop once the challenge is completed
                                    break  # Exit the for loop

                            elif (game_state.spot, game_state.orientation) in kakachi_gang_challenge_conditions and kakachi_gang_challenge_conditions[(game_state.spot, game_state.orientation)] and kakachi_gang_trigger:
                                if counterk - 3 < kakachi_gang_spots:

                                    # Dice dict

                                    enemy = counterk + 1

                                    phrase_dict_gde = phrase_dicts_gde[counterk]
                                    phrase_dict_moy = phrase_dicts_moy[counterk]
                                    phrase_dict_pet = phrase_dicts_pet[counterk]
                                    sound_dict = sound_dicts[counterk]
                                    etext = enemy_text[counterk]

                                    # Loop until the user succeeds
                                    while not special_enemy(
                                        decoy, etext, user_lives, enemy_lives, enemy, enemy_alive, game_state.spot, game_state.orientation,
                                        nextimage, phrase_dict_gde, phrase_dict_moy, phrase_dict_pet, sound_dict, sound,
                                        display_nal, kakachi_gang_challenge_conditions, clean_input, WHITE_HEIGHT,
                                        k, ctrl_pressed, display_f_text, display_s_text
                                    ):
                                        pass  # Loop until the user succeeds
                                    
                                    counterk = counterk + 1
                                    one = False  # Exit the loop once the challenge is completed
                                    break  # Exit the for loop

                            elif (game_state.spot, game_state.orientation) in kakachi_challenge_conditions and kakachi_challenge_conditions[(game_state.spot, game_state.orientation)]:
                                # Loop until the user succeeds
                                sound_dict = sound_dict7
                                enemy = 7
                                etext = kakachi_text
                                while not special_enemy(
                                    decoy, etext, user_lives, enemy_lives, enemy, enemy_alive, game_state.spot, game_state.orientation,
                                    nextimage, phrase_dict_gde_kakachi, phrase_dict_moy_kakachi, phrase_dict_pet_kakachi, sound_dict, sound,
                                    display_nal, kakachi_challenge_conditions, clean_input, WHITE_HEIGHT,
                                    k, ctrl_pressed, display_f_text, display_s_text
                                ):
                                    pass  # Loop until the user succeeds
                                
                                kakachi_gang_trigger = True
                                one = False  # Exit the loop once the challenge is completed
                                break  # Exit the for loop


                            elif game_state.spot in shield_challenge_spots and shield_challenge_conditions[game_state.spot]:
                                # !!! ADJUST (give phrase x to this challenge)
                                if not special_shield(game_state.spot, nextimage, special_dict['phrase3'], sound, display_nal, shield_challenge_conditions, clean_input, decoy, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive, k, ctrl_pressed, display_w_text):
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

                    else:
                        input_text += event.unicode

                    if display_w_text:
                        wrong_words_str = ', '.join(wrong_words)
                        display_nal(nextimage, "Commande non reconnue. Tapez 'info' puis Entrée pour voir les commandes." + wrong_words_str, "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                
                    else:
                        display_nal(nextimage, text, "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

                    pygame.display.flip()
                
                elif event.type == KEYUP and ctrl_pressed and event.key == K_q:
                    quit_level = True
                    all_running = False
                    return

                elif event.type == KEYUP and event.key in (K_LCTRL, K_RCTRL):
                    ctrl_pressed = False


    ## Intro Part

    # Start screen: picture + instructions (modules3/intro_screen.py)
    intro_title = 'MISSION 3 – Évasion du Lavish Lair'
    intro_lines = [
        "Récupérez les clés de la voiture (sûrement à la bibliothèque) et un Nuka-Cola bien frais (aux cuisines... mais Kakachi le veut aussi !), puis tapez le code des clés à l'entrée (votre point de départ).",
        "- Bouger : tapez 'avant', 'gauche', 'droite' ou 'arrière', puis Entrée. Fouiller : tapez 'fouiller' puis Entrée.",
        "- Combats : Ctrl + 1, 2 ou 3 pour écouter une phrase courte, moyenne ou longue. Tapez le numéro de votre arme, un point, puis la phrase : '1.' pistolet (-1 vie, 2 balles), '2.' mitraillette (-2 vies), '3.' shotgun (-3 vies, 1 cartouche). Exemple : '2. le chat dort'",
        '- Chaque phrase ratée vous coûte un de vos 4 cœurs. Sans cœur, le combat recommence.',
        "- Mip-mip ! = vous avez oublié le numéro de l'arme ('1.', '2.' ou '3.') au début.",
        "- Bip-bip ! = le mot que vous venez de taper est faux (le jeu vérifie chaque mot quand vous appuyez sur la barre d'espace) : corrigez-le avant de continuer.",
        "- Tapez 'info' puis Entrée à tout moment pour voir les commandes. 'quitter' pour revenir au menu.",
    ]
    intro_footer = 'Appuyez sur une touche pour commencer !'
    show_intro(screen, load.get('lobby'), intro_title, intro_lines, intro_footer, WIDTH, HEIGHT)
    sound["bus_debut_"].play()


    ## Main part

    # Main loop
    while all_running:
        main(decoy, edoc)

    if quit_level:
        return


    ## Outro part

    # Final message display
    display_nal(load.get('final'), "Mission 3. Félicibravotation !!! Vous avez terminé la mission 3 de la 'Bataille Royale du Français', le premier Text-Based Game to Improve Your Writing Skills, co-developpé par Aichi Panchu et la Rascasse de l'Espace. Spéciale dédicace à PapyCat pour l'inspiration et, bien sûr, Robert le Phacochère, notre mascotte officielle. Et comme l'a bien dit notre indispensable collaborateur, ChatGPT: \"Nezourez pas le code c'est du caca !!!\"", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

    # Wait for quit event
    while True:
        pygame.init()
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                return

### TO REMOVE        
#lvl3('test', 'tset')