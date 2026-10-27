# Status: W:  
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
from modulesu.load_images_mov import load_images_mov
from modulesu.draw_wrap_clean import draw_text, wrap_text, clean_input
from modulesu.special_searchoff import special_searchoff
from modulesu.special_shield import special_shield
from modulesu.special_trap import special_trap
from modulesu.special_enemy import special_enemy
from modulesu.load_sounds import load_sounds
from modulesu.load_images_oth import ImageLoader
from modulesu.phrases_extract_other import other_phrases
from modulesu.phrases_extract_moyennes import moyennes_phrases
from modulesu.load_images_enemy import ImageLoaderEnemy
from modulesu.load_sounds_enemy import load_sounds_enemy
from modulesu.random_dice import random_dice
from modulesu.intro_screen import show_intro
from modulesu.city_map import draw_city_map
from modulesu.special_animal import special_animal
from modulesu.data_import import import_data_all, import_quest
from modulesu.locations_coordinates import locations, zones
import importlib.util
import shutil
import os

def lvlu(saved_game='', quest_file=None):

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

    animal_phrase_gde_path = 'files/texts/conjugaisons_gde.txt'
    animal_phrase_moy_path = 'files/texts/conjugaisons_moy.txt'
    animal_phrase_pet_path = 'files/texts/conjugaisons_pet.txt'

    ### Variables

    # Globalize
    global nextimage, all_running, search_challenge_conditions, enemy, enemy_counter, counterk
    global user_lives, enemy_lives, enemy, enemy_counter, counterk 
    global enemy_alive, enemy_spots, random_mapping, boss_lives
    global objective1, objective2, objective3, everest_mode, everest_count
    global evytext, search_counter, search_riddle1, search_riddle2, search_riddle3, search_riddle4, search_riddle5

    ### AHHHHHHHHHHHHHHHHHHHHHHH ####
    objective1 = objective2 = objective3 = False

    if saved_game == 'y':

        with open(f'files/saves/save.txt', 'r') as file:
            content_load = file.read().strip()
            saved_data = content_load[:2]
            load_objectives = content_load[2:].strip()

        # Import specific data
        folder_path = os.path.join(os.path.dirname(__file__), 'files/data')
        file_path = os.path.join(folder_path, f"data{saved_data}.py")
        module_name = f"data{saved_data}"
            
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        data_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(data_module)

        data_all = data_module.data_all
        folder_path = os.path.join(os.path.dirname(__file__))

        
        sco_list = load_objectives.splitlines()

        objective1 = '491' in sco_list
        objective2 = '512' in sco_list
        objective3 = '723' in sco_list

    else:    
        # Import data
        directory_data = 'files/data'
        if quest_file:  # quest chosen in the menu ('4a', '4b'...)
            data_all = import_quest(directory_data, quest_file)
        else:
            data_all = import_data_all(directory_data)  # a different quest each time (see modulesu/data_import.py)

    (
        # Data ID
        data_id,
        quest_title,
        
        # Number of Enemies
        enemy_spots,

        # ID of Boss
        boss,

        # ID of Enemies
        enemy1,
        enemy2,
        enemy3,
        enemy4,
        enemy5,

        # Number of Events
        search_spots,

        # Text (characters)
        enemy_text1,
        enemy_text2,
        enemy_text3,
        enemy_text4,
        enemy_text5,
        boss_text,
        boss_netext,
        enemy_position,
        boss_position,

        # Text (objectives)
        text_all, 
        text_1,
        text_2,
        text_3,
        text_12,
        text_13,
        text_23,
        text_finish, 

        # Text (decoy, edoc)
        decoy,
        edoc,

        # Zones
        d_trap_pool, 
        d_shield_pool, 
        d_search_pool, 
        d_enemy_pool,
        d_boss_pool,

        # Specific locations
        d_spec_location1,
        d_spec_location2,
        d_spec_location3,
        d_spec_location4,
        d_spec_location5,

        # Specific real items
        item1,
        item2,
        item3,
        item4,
        item5,

        # Specific fake1 items
        fake1item1,
        fake1item2,
        fake1item3,
        fake1item4,
        fake1item5,

        # Specific fake2 items
        fake2item1,
        fake2item2,
        fake2item3,
        fake2item4,
        fake2item5,

        # Specific riddles texts
        search_riddle1,
        search_riddle2,
        search_riddle3,
        search_riddle4,
        search_riddle5,

        # Specific item position
        position_item1,
        position_item2,
        position_item3,
        position_item4,
        position_item5,

        # Specific fake1 item position
        position_fake1item1,
        position_fake1item2,
        position_fake1item3,
        position_fake1item4,
        position_fake1item5,

        # Specific fake2 item position
        position_fake2item1,
        position_fake2item2,
        position_fake2item3,
        position_fake2item4,
        position_fake2item5,

        # Specific initialize searches texts
        init_search_text1,
        init_search_text2,
        init_search_text3,
        init_search_text4,
        init_search_text5,

        # Specific searches texts
        search_text1,
        search_text2,
        search_text3,
        search_text4,
        search_text5,

        # Sound (av, co, db, etc.)
        tag1,
        tag2,
        tag3,
        tag4,
        tag5,
        tagboss

    ) = (

    # Data ID
    data_all["data_id"],
    data_all["quest_title"],

    # Number of Enemies
    data_all["enemy_spots"],

    # ID of Boss
    data_all["boss"],

    # ID of Enemies
    data_all["enemy1"],
    data_all["enemy2"],
    data_all["enemy3"],
    data_all["enemy4"],
    data_all["enemy5"],

    # Number of Events
    data_all["search_spots"],

    # Text (characters)
    data_all["enemy_text1"],
    data_all["enemy_text2"],
    data_all["enemy_text3"],
    data_all["enemy_text4"],
    data_all["enemy_text5"],
    data_all["boss_text"],
    data_all["boss_netext"],
    data_all["enemy_position"],
    data_all["boss_position"],

    # Text (objectives)
    data_all["text_all"],
    data_all["text_1"],
    data_all["text_2"],
    data_all["text_3"],
    data_all["text_12"],
    data_all["text_13"],
    data_all["text_23"],
    data_all["text_finish"],

    # Text (decoy, edoc)
    data_all["decoy"],
    data_all["edoc"],

    # Zones
    data_all["d_trap_pool"],
    data_all["d_shield_pool"],
    data_all["d_search_pool"],
    data_all["d_enemy_pool"],
    data_all["d_boss_pool"],

    # Specific locations; 'none' if none
    data_all["d_spec_location1"],
    data_all["d_spec_location1"],
    data_all["d_spec_location1"],
    data_all["d_spec_location1"],
    data_all["d_spec_location1"],

    # Specific real items
    data_all["item1"],
    data_all["item1"],
    data_all["item1"],
    data_all["item1"],
    data_all["item1"],

    # Specific fake1 items
    data_all["fake1item1"],
    data_all["fake1item1"],
    data_all["fake1item1"],
    data_all["fake1item1"],
    data_all["fake1item1"],

    # Specific fake2 items
    data_all["fake2item1"],
    data_all["fake2item1"],
    data_all["fake2item1"],
    data_all["fake2item1"],
    data_all["fake2item1"],

    # Specific riddles texts
    data_all['search_riddle1'],
    data_all['search_riddle1'],
    data_all['search_riddle1'],
    data_all['search_riddle1'],
    data_all['search_riddle1'],

    # Specific item position
    data_all["position_item1"],
    data_all["position_item1"],
    data_all["position_item1"],
    data_all["position_item1"],
    data_all["position_item1"],

    # Specific fake1 item position
    data_all["position_fake1item1"],
    data_all["position_fake1item1"],
    data_all["position_fake1item1"],
    data_all["position_fake1item1"],
    data_all["position_fake1item1"],

    # Specific fake2 item position
    data_all["position_fake2item1"],
    data_all["position_fake2item1"],
    data_all["position_fake2item1"],
    data_all["position_fake2item1"],
    data_all["position_fake2item1"],

    # Specific initialize searches texts
    data_all["init_search_text1"],
    data_all["init_search_text1"],
    data_all["init_search_text1"],
    data_all["init_search_text1"],
    data_all["init_search_text1"],

    # Specific searches texts
    data_all["search_text1"],
    data_all["search_text1"],
    data_all["search_text1"],
    data_all["search_text1"],
    data_all["search_text1"],

    # Sound (av, co, db, etc.)
    data_all["tag1"],
    data_all["tag2"],
    data_all["tag3"],
    data_all["tag4"],
    data_all["tag5"],
    data_all["tagboss"]
    )

    if saved_game != 'y':
        with open('files/saves/save.txt', 'w') as file:
            content_ID = f'{data_id}\n'
            file.write(content_ID)

    # Boss
    boss_spot = 1

    # Events
    trap_spots = 2
    shield_spots = 2

    # Enemies
    enemies_list = [enemy1, enemy2, enemy3, enemy4, enemy5]
    enemies_text = [enemy_text1, enemy_text2, enemy_text3, enemy_text4, enemy_text5]

    # Sounds for Enemies and Boss already in lists below
    #         sound_dict_enemy1, 2, etc, sound_dict_boss

    # Searches: each search i (1..search_spots) has its own place, objects, riddle and texts
    def quest_list(prefix, default=None, suffix=''):
        return [data_all.get(f'{prefix}{i}{suffix}', default) for i in range(1, 6)]
    spec_location_list = quest_list('d_spec_location', 'none')
    (init_search_text1, init_search_text2, init_search_text3, init_search_text4, init_search_text5) = quest_list('init_search_text', '')
    (search_text1, search_text2, search_text3, search_text4, search_text5) = quest_list('search_text', '')
    (item1, item2, item3, item4, item5) = quest_list('item', 'none')
    (fake1item1, fake1item2, fake1item3, fake1item4, fake1item5) = quest_list('fake1item', 'none')
    (fake2item1, fake2item2, fake2item3, fake2item4, fake2item5) = quest_list('fake2item', 'none')
    (search_riddle1, search_riddle2, search_riddle3, search_riddle4, search_riddle5) = quest_list('search_riddle', '')
    (position_item1, position_item2, position_item3, position_item4, position_item5) = quest_list('position_item', (300, 300))
    (position_fake1item1, position_fake1item2, position_fake1item3, position_fake1item4, position_fake1item5) = quest_list('position_fake1item', (500, 300))
    (position_fake2item1, position_fake2item2, position_fake2item3, position_fake2item4, position_fake2item5) = quest_list('position_fake2item', (700, 300))
    search_spots = min(search_spots, 4)  # 4 sets of search sentences are prepared below

    init_search_text_list = [init_search_text1, init_search_text2, init_search_text3, init_search_text4, init_search_text5]
    search_text_list = [search_text1, search_text2, search_text3, search_text4, search_text5]
    
    item_list = [item1, item2, item3, item4, item5]
    fake1item_list = [fake1item1, fake1item2, fake1item3, fake1item4, fake1item5]
    fake2item_list = [fake2item1, fake2item2, fake2item3, fake2item4, fake2item5]
    activate_item_list = [False, False, False, False, False]

    position_item_list = [position_item1, position_item2, position_item3, position_item4, position_item5]
    position_fake1item_list = [position_fake1item1, position_fake1item2, position_fake1item3, position_fake1item4, position_fake1item5]
    position_fake2item_list = [position_fake2item1, position_fake2item2, position_fake2item3, position_fake2item4, position_fake2item5]
 
    # Pool zones
    trap_pool = zones.get(d_trap_pool)
    shield_pool = zones.get(d_shield_pool)
    search_pool = zones.get(d_search_pool)
    enemy_pool = zones.get(d_enemy_pool)
    boss_pool = zones.get(d_boss_pool)

    # Specific locations attributed after randomizer

    # Lives / Modes
    user_lives = 4
    enemy_lives = 3 # careful, they're redefined = x in main
    boss_lives = 3
    
    enemy_alive = 1 # samesies
    everest_mode = False
    everest_count = 3

    # Counters
    enemy = 0
    enemy_counter = enemy_spots
    search_counter = search_spots

    # Enemy dictionary (can't name because of [i] system)
    # 1: group 1 enemy 1; 2 -> 5: idem; 6: boss; 7: everest 
    # 11 -> 15: group 2 enemy; 21 -> 25: group 3 enemy

    # Starting point of the Ultimate Mission (spot 9 = crossroads in the middle of the map,
    # between the houses, the park and the shops). It used to be spot 1.
    START_SPOT, START_ORIENTATION = 9, 1
    protected_spots = [START_SPOT]  # Spots to protect (no trap / shield / enemy on the starting point)

    num_spots = 55
    num_orientations = 4
    
    # Phrases and Conjugations preparation
    num_phr_per = enemy_spots
    num_phr_per_animal = 3

    # 3 pour special, 1 pour boss
    num_phr_tot_moy = 3 * enemy_spots
    num_phr_tot_gde = num_phr_tot_pet = 3 * enemy_spots

    num_phr_tot_moy_animal = 3 + 3 + 3
    num_phr_tot_gde_animal = num_phr_tot_pet_animal = 3 + 3 + 3

    # Phrases
    # enemy (5) boss (1) search (4) shield (3) trap (3) 
    (
        phrase_dict_moy_enemy1, phrase_dict_moy_enemy2, phrase_dict_moy_enemy3, 
        phrase_dict_moy_enemy4, phrase_dict_moy_enemy5, 
        phrase_dict_moy_boss,
        phrase_dict_moy_search1, phrase_dict_moy_search2, phrase_dict_moy_search3, 
        phrase_dict_moy_search4, 
        phrase_dict_moy_shield1, phrase_dict_moy_shield2, phrase_dict_moy_shield3, 
        phrase_dict_moy_trap1, phrase_dict_moy_trap2, phrase_dict_moy_trap3

    ) = moyennes_phrases(16, enemy_phrase_moy_path, 48, 3)

    # enemy (5) boss (1)
    (
        phrase_dict_gde_enemy1, phrase_dict_gde_enemy2, phrase_dict_gde_enemy3,
        phrase_dict_gde_enemy4, phrase_dict_gde_enemy5, phrase_dict_gde_boss,

    )  = other_phrases(enemy_phrase_gde_path, 18, 3)

    # enemy (5) boss (1)    
    (
        phrase_dict_pet_enemy1, phrase_dict_pet_enemy2, phrase_dict_pet_enemy3, 
        phrase_dict_pet_enemy4, phrase_dict_pet_enemy5, 
        phrase_dict_pet_boss

    ) = other_phrases(enemy_phrase_pet_path, 18, 3)
    
    phrase_dicts_moy_enemy = (
        phrase_dict_moy_enemy1, phrase_dict_moy_enemy2, phrase_dict_moy_enemy3, 
        phrase_dict_moy_enemy4, phrase_dict_moy_enemy5) 

    phrase_dicts_moy_shield = (
        phrase_dict_moy_shield1, phrase_dict_moy_shield2, phrase_dict_moy_shield3)

    phrase_dicts_moy_trap = (
        phrase_dict_moy_trap1, phrase_dict_moy_trap2, phrase_dict_moy_trap3)

    phrase_dicts_moy_search = (
        phrase_dict_moy_search1, phrase_dict_moy_search2, phrase_dict_moy_search3, 
        phrase_dict_moy_search4)

    phrase_dicts_gde_enemy = (
        phrase_dict_gde_enemy1, phrase_dict_gde_enemy2, phrase_dict_gde_enemy3,
        phrase_dict_gde_enemy4, phrase_dict_gde_enemy5)

    phrase_dicts_pet_enemy = (
        phrase_dict_pet_enemy1, phrase_dict_pet_enemy2, phrase_dict_pet_enemy3, 
        phrase_dict_pet_enemy4, phrase_dict_pet_enemy5)

    # Conjugations
    (
        conj_dict_pet_animal1, conj_dict_pet_animal2, conj_dict_pet_animal3, 
        conj_dict_pet_boss, 
        filler_dict_pet5, filler_dict_pet6

    ) = other_phrases(animal_phrase_pet_path, 18, 3)
    
    (
        conj_dict_moy_animal1, conj_dict_moy_animal2, conj_dict_moy_animal3, 
        conj_dict_moy_boss
        
    ) = moyennes_phrases(4,animal_phrase_moy_path, 18, 3)
 
    (
        conj_dict_gde_animal1, conj_dict_gde_animal2, conj_dict_gde_animal3, 
        conj_dict_gde_boss, 
        filler_dict_gde5, filler_dict_gde6
        
    ) = other_phrases(animal_phrase_gde_path, 18, 3)
 
    conj_dicts_pet_animal = (
        conj_dict_pet_animal1, conj_dict_pet_animal2, conj_dict_pet_animal3)

    conj_dicts_moy_animal = (
        conj_dict_moy_animal1, conj_dict_moy_animal2, conj_dict_moy_animal3)

    conj_dicts_gde_animal = (
        conj_dict_gde_animal1, conj_dict_gde_animal2, conj_dict_gde_animal3)

    edoc1 = edoc[:2]
    edoc2 = edoc[2:][:2]
    edoc3 = edoc[4:]

    # Static texts
    evytext = "Oh mon dieu, Everest libère littéralement le tigre qui est en elle (et puis j'avais pas de photo d'elle comme ça, alors hein, bon) et ne fait qu'une bouchée de son ennemi. Un tel appétit, ça fait plaisir à voir."
    etext_evy = "Everest n'a pas l'air très motivée à se battre, mais des petites gâteries pourraient la convaincre : conjuguez ! 'Ctrl + 1', '+ 2' ou '+ 3' vous donne un verbe et un temps. Tapez ensuite '1.' et le verbe avec je et tu, '2.' avec je, tu, il/elle, nous, ou '3.' avec je, tu, il/elle, nous, vous, ils/elles."
    netext_evy = "Ouiiii! Vous avez réussi, Everest est folle, elle tourne sur elle-même en essayant d'attraper sa queue, elle fait des saltos de côté, elle hurle à la lune alors qu'il est midi, elle joue du banjo avec un chapeau... ah non, là j'abuse un peu. En tout cas, elle est prête à bouffer de l'ennemi ! Devant le prochain ennemi, tapez 'e. attaque' pour la lâcher !"
    die_text = "Oh oh oh (non pas le Père Noël, juste de l'étonnement), le boss tourne sur lui-même elle-même, il fait des saltos de côté... mince, je suis en train de recopier le text d'Éverest. Il tourne et il tombe tel un... truc qui tombe... une pomme? Bref, il a l'air mort... non, je vous jure, il a l'air mort... mort mort mort."
    revive_text = "Comment, il est pas mort ? Il est revenu à la vie ! Achevez-le avec une conjugaison : 'Ctrl + 1', '+ 2' ou '+ 3' vous donne un verbe et un temps. Tapez ensuite '1.' et le verbe avec je et tu, '2.' avec je, tu, il/elle, nous, ou '3.' avec je, tu, il/elle, nous, vous, ils/elles."

    random_mapping = random_dice()

    ### Load images
    # !!! ADJUST (mov: dans script load_images_mov)
    images = load_images_mov(num_spots, num_orientations)

    # !!! ADJUST (mov: dans script load_images_oth)
    folder_path = 'files/images_oth'
    items_path = 'files/items'
    enemy_folder_path = 'files/new_enemies'
    load = ImageLoader(folder_path)
    load_items = ImageLoader(items_path)
    load_enemy = ImageLoaderEnemy(enemy_folder_path)

    # Define paths to the image and sound folders
    sound_folder = 'files/sound_enemy'
    tageverest = '7'

    (
        sound_dict_enemy1, sound_dict_enemy2, sound_dict_enemy3,
        sound_dict_enemy4, sound_dict_enemy5, 
        sound_dict_boss, sound_dict_animal
         
    ) = load_sounds_enemy(sound_folder, tag1, tag2, tag3, tag4, tag5, tagboss, tageverest)
    
    sound_dicts_enemy = (
        sound_dict_enemy1, sound_dict_enemy2, sound_dict_enemy3,
        sound_dict_enemy4, sound_dict_enemy5)

    # Set the transparency level (alpha) for the overlay
    load.get('trap').set_alpha(130)

    ### Dictionary to store game states
    nextimage = load.get('lobby')
    all_running = True
    one = True
    k = K_1
    ff = 'full flemme'

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
    from modulesu.gamestate import GameState
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
    #gang_challenge_conditions = {}
    boss_challenge_conditions = {}


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

    # Search places (one or more states per place) and their search number
    search_spots_orientations = []
    search_index = {}
    for i, location in enumerate(spec_location_list[:search_spots]):
        for state in locations.get(location, []):
            search_spots_orientations.append(state)
            search_index[state] = i

    # Boss: at a fixed place when the quest gives one ('boss_location'), otherwise random in its zone
    boss_location = data_all.get('boss_location', 'none')
    fixed_boss = locations.get(boss_location, [None])[0] if boss_location != 'none' else None

    # No trap / shield / enemy on the start, on a search place or on the boss place
    no_event_spots = set(protected_spots) | {s for s, o in search_spots_orientations}
    if fixed_boss:
        no_event_spots.add(fixed_boss[0])

    # Remove protected spots from pools
    trap_pool = [spot for spot in trap_pool if spot not in no_event_spots]
    shield_pool = [spot for spot in shield_pool if spot not in no_event_spots]
    search_pool = [spot for spot in search_pool if spot not in no_event_spots]
    enemy_pool = [spot for spot in enemy_pool if spot not in no_event_spots]
    boss_pool = [spot for spot in boss_pool if spot not in set(protected_spots)]

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

    # Enemy challenge spots
    enemy_spots_orientations = generate_unique_spot_orientations(enemy_spots, enemy_pool, num_orientations, game_state)
    if fixed_boss:
        boss_spot_orientation = [fixed_boss]
    else:
        boss_spot_orientation = generate_unique_spot_orientations(boss_spot, boss_pool, num_orientations, game_state)

    # Store enemy spot orientations in a dictionary
    for spot, orientation in enemy_spots_orientations:
        enemy_challenge_conditions[(spot, orientation)] = True  # Initially set to True or False based on game logic

    def set_enemy_conditions(spot, orientation, status):
        enemy_challenge_conditions[(spot, orientation)] = status

    # Update enemy_challenge_conditions based on save
    if saved_game == 'y':
        # enemies already beaten before the save: remove them and count them
        # (enemies are fought from the last one of the list to the first one)
        for index, saved_enemy in enumerate(enemies_list[:enemy_spots]):
            if saved_enemy in sco_list:
                spot, orientation = enemy_spots_orientations[index]
                set_enemy_conditions(spot, orientation, False)
                enemy_counter -= 1
                
    for location in boss_spot_orientation:
        boss_challenge_conditions[location] = True

    for location in search_spots_orientations:
        search_challenge_conditions[location] = True

    # Update search_challenge_conditions based on save
    if saved_game == 'y':
        done_searches = {i for state, i in search_index.items() if f'search {state[0]}_{state[1]}' in sco_list}
        for state, i in search_index.items():
            if i in done_searches:
                search_challenge_conditions[state] = False
        search_counter -= len(done_searches)

    ### display_nal: Function to display text and images
    def display_nal(image, displayed_text, typed_text, wrectangle, enemy_lives, user_lives, enemy, enemy_alive):
        if enemy_lives < 0:
            enemy_lives = 0
        
        if enemy == 7:
            modulus = (3 - enemy_lives)
            elives_str = f'elives{modulus}'
        else:
            elives_str = f'elives{enemy_lives}'
        
        ulives_str = f'ulives{user_lives}'
        scratchesd_str = f'scratchesd{user_lives}'
        scratchesc_str = f'scratchesc{user_lives}'
        ulives_str = f'ulives{user_lives}'

        if enemy_lives > 0:
            enemy_alive = 1
        else:
            enemy_alive = 0

        if enemy == 7:
            enemy_str = 'evyprep'
        else:
            enemy_str = f'{enemy}{enemy_alive}'
        
        screen.blit(image, (0, 0))


        if enemy !=7:
            if displayed_text != evytext:
                screen.blit(load.get('evy'), (450, HEIGHT - 125 - load.get('evy').get_height() + 25))
            else:
                screen.blit(load.get('tiger'), (1 * WIDTH // 2 - load_enemy.get_enemy(enemy_str).get_width() // 2, 2 * HEIGHT // 5 - load_enemy.get_enemy(enemy_str).get_height() // 2))

        elif displayed_text == netext_evy:
            screen.blit(load.get('evyprep'), (450, HEIGHT - 125 - load.get('evyprep').get_height() + 25))
            screen.blit(load.get('prepped1'), (250, HEIGHT - 125 - 200 - load.get('prepped1').get_height() + 25))
            screen.blit(load.get('prepped2'), (450, HEIGHT - 125 - 300 - load.get('prepped2').get_height() + 25))
            screen.blit(load.get('prepped3'), (550, HEIGHT - 125 - 200 - load.get('prepped3').get_height() + 25))

        else:
            screen.blit(load.get('evyprep'), (450, HEIGHT - 125 - load.get('evyprep').get_height() + 25))

        #if displayed_text != etext_evy:

        screen.blit(load.get('character'), (250, HEIGHT + 7 - 125 - load.get('character').get_height() + 25))
        screen.blit(load.get(ulives_str), (700, 515))

        # Searches Item Blit
        if (game_state.spot, game_state.orientation) in search_challenge_conditions:
            blit_index = search_index[(game_state.spot, game_state.orientation)]
            if activate_item_list[blit_index] == True and search_challenge_conditions[(game_state.spot, game_state.orientation)]:
                true_object = item_list[blit_index]
                false1_object = fake1item_list[blit_index]
                false2_object = fake2item_list[blit_index]
                position_real_object = position_item_list[blit_index]
                position_false1_object = position_fake1item_list[blit_index]
                position_false2_object = position_fake2item_list[blit_index]
                
                screen.blit(load_items.get(true_object), (position_real_object))
                screen.blit(load_items.get(false1_object), (position_false1_object))
                screen.blit(load_items.get(false2_object), (position_false2_object))

        elif game_state.spot in shield_challenge_spots and shield_challenge_conditions[game_state.spot]:
            screen.blit(load.get('shield'), (0, 0))

        elif game_state.spot in trap_challenge_spots and trap_challenge_conditions[game_state.spot]:
            screen.blit(load.get('trap'), (0, 0))
       
        elif (game_state.spot, game_state.orientation) in enemy_challenge_conditions and enemy_challenge_conditions[(game_state.spot, game_state.orientation)]:
            # !!! Adjust position hearts with respect to image, not absolute, and find correct
            screen.blit(load.get(elives_str), (1 * WIDTH // 2 - load.get(elives_str).get_width() // 2, 2 * HEIGHT // 5 - load_enemy.get_enemy(enemy_str).get_height() // 2 - load.get(elives_str).get_height() + 100))
            screen.blit(load_enemy.get_enemy(enemy_str), (1 * WIDTH // 2 - load_enemy.get_enemy(enemy_str).get_width() // 2, 2 * HEIGHT // 5 - load_enemy.get_enemy(enemy_str).get_height() // 2 + 100))
            if enemy !=7 and displayed_text == evytext:
                screen.blit(load.get('tiger'), (1 * WIDTH // 2 - load_enemy.get_enemy(enemy_str).get_width() // 2, 2 * HEIGHT // 5 - load_enemy.get_enemy(enemy_str).get_height() // 2))


        elif (game_state.spot, game_state.orientation) in boss_challenge_conditions and boss_challenge_conditions[(game_state.spot, game_state.orientation)] and enemy == boss:
            # Only drawn during the fight with the chief (before, his hearts showed up alone at his spot)
            # !!! Adjust position hearts with respect to image, not absolute, and find correct
            screen.blit(load.get(elives_str), (1 * WIDTH // 2 - load.get(elives_str).get_width() // 2, 2 * HEIGHT // 5 - load_enemy.get_enemy(enemy_str).get_height() // 2 - load.get(elives_str).get_height() + 100))
            screen.blit(load_enemy.get_enemy(enemy_str), (1 * WIDTH // 2 - load_enemy.get_enemy(enemy_str).get_width() // 2, 2 * HEIGHT // 5 - load_enemy.get_enemy(enemy_str).get_height() // 2 + 100))
            screen.blit(load.get(ulives_str), (700, 515))
            if user_lives in [1,2,3] and enemy == 7:
                screen.blit(load.get(scratchesc_str), (0,0))

        font = pygame.font.Font(None, 26)
        
        # Wrap Naruto's text
        info_lines = []
        for paragraph in displayed_text.split('\n'):
            info_lines.extend(wrap_text(paragraph, font, WIDTH - 20))

        for i, line in enumerate(info_lines):
            draw_text(screen, line, (10, HEIGHT - wrectangle + 34 + i * font.get_linesize()), font)

        # Wrap Player's text
        player_lines = []
        for paragraph in typed_text.split('\n'):
            player_lines.extend(wrap_text(paragraph, font, WIDTH - 20))

        player_start_pos = HEIGHT - wrectangle + (len(info_lines) * font.get_linesize()) + 40
        for i, line in enumerate(player_lines):
            draw_text(screen, line, (10, player_start_pos + i * font.get_linesize()), font)

        pygame.display.flip()

    # !!! ADJUST
    # Set starting position (adjust as per your game's requirement)
    game_state = GameState(spot=START_SPOT, orientation=START_ORIENTATION)

    # Initialize pygame and other necessary components
    pygame.init()

    text_controls = "COMMANDES : flèches ou W A S D pour bouger (haut = avancer, gauche / droite = tourner, bas = demi-tour). Tapez puis Entrée : 'fouiller', 'titre', 'énigme1' (l'énigme), 'ennemi' et 'chef' (indices), 'ville' (plan), 'evy' (Everest). 'info' pour revenir aux objectifs, 'quitter' pour sauvegarder et revenir au menu."
    cmd_info = ['info', 'commandes', 'aide']
    cmd_quit = ['quitter', 'menu']
    help_state = {'controls': False}
    quit_state = {'quit': False}
    map_state = {'on': False}  # city map shown with 'ville'
    text_map = "PLAN DE LA VILLE : la flèche rouge, c'est vous (elle pointe là où vous regardez). On ne peut pas bouger tant que le plan est ouvert : tapez encore 'ville' (ou Échap) pour revenir à la rue."

    def display_city(typed_text):
        """City map (modulesu/city_map.py) instead of the street picture, with the usual white band."""
        screen.fill((255, 255, 255))
        draw_city_map(screen, game_state.connections, game_state.spot, game_state.orientation, 'fr', (0, 0, WIDTH, HEIGHT - WHITE_HEIGHT))
        font = pygame.font.Font(None, 26)
        info_lines = wrap_text(text_map, font, WIDTH - 20)
        for i, line in enumerate(info_lines):
            draw_text(screen, line, (10, HEIGHT - WHITE_HEIGHT + 34 + i * font.get_linesize()), font)
        player_start_pos = HEIGHT - WHITE_HEIGHT + (len(info_lines) * font.get_linesize()) + 40
        for i, line in enumerate(wrap_text(typed_text, font, WIDTH - 20)):
            draw_text(screen, line, (10, player_start_pos + i * font.get_linesize()), font)
        pygame.display.flip()

    ### Mots de la semaine
    phrase_dict_moy_trap1 = "l'apprenti saute les barrières mais a la grippe"
    phrase_dict_moy_shield1 = "la lutte est en apparence comme les colles"
    # same clean-up as the sentence files (lower case, straight apostrophes, single spaces)
    phrase_dict_moy_trap1 = ' '.join(phrase_dict_moy_trap1.replace('\u2019', "'").split()).lower()
    phrase_dict_moy_shield1 = ' '.join(phrase_dict_moy_shield1.replace('\u2019', "'").split()).lower()

    ## Main function
    def main(decoy, edoc):
        global nextimage, all_running, search_challenge_conditions, enemy, enemy_counter, counterk, companion_trigger
        global objective1, objective2, objective3, enemy_text, enemy_text_ko, sound_dicts, tele, instru_tele, everest_count
        global evytext, everest_mode, search_counter, search_riddle1, search_riddle2, search_riddle3, search_riddle4, search_riddle5

        input_text = ''
        display_w_text = False
        display_f_text = False
        display_s_text = False
        one = True
        ctrl_pressed = False
        wrong_words = []
        map_state['on'] = False  # after a challenge or 'info', back to the street view

        user_lives = 4
        enemy_lives = 3
        boss_lives = 3

        # Objectives texts
        if objective1:
            if objective2:
                if objective3:
                    text = text_finish
                else:
                    text = text_3
            elif objective3:
                text = text_2
            else:
                text = text_23

        elif objective2:
            if objective3:
                text = text_1
            else:
                text = text_13

        elif objective3:
            text = text_12

        else:
            text = text_all

        if help_state['controls']:
            text = text_controls

        # Success
        if objective1 and objective2 and objective3:
            sound['tacos'].play()
            all_running = False
            one = False
            return

        tele = load.get('tele')

        nextimage = images[f"{game_state.spot}_{game_state.orientation}"]
        if (game_state.spot, game_state.orientation) in enemy_spots_orientations:
            display_nal(nextimage, text, "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
        else:
            display_nal(nextimage, text, "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

        while one:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        cleaned_input = clean_input(input_text)

                        if cleaned_input in cmd_info:
                            help_state['controls'] = not help_state['controls']
                            one = False
                            break  # main() is called again and shows the right text

                        if cleaned_input in cmd_quit:
                            quit_state['quit'] = True
                            all_running = False
                            return

                        if cleaned_input in [decoy, ff, edoc, 'fouiller', 'ville', 'evy', 'énigme1', 'énigme2', 'énigme3', 'énigme4', 'énigme5', 'ennemi', 'chef', 'titre']:
                            if cleaned_input == 'ville':  # city map on / off
                                sound['magik'].play()
                                map_state['on'] = not map_state['on']
                                input_text = ''
                                display_w_text = False
                                if map_state['on']:
                                    display_city('')
                                else:
                                    display_nal(nextimage, text, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                continue

                            map_state['on'] = False  # any other command: back to the street view

                            if cleaned_input == 'titre':
                                    sound['magik'].play()
                                    display_nal(nextimage, quest_title, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue

                            if cleaned_input == 'ennemi':
                                sound['magik'].play()
                                display_nal(nextimage, enemy_position, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                input_text = ''
                                continue

                            if cleaned_input == 'chef':
                                sound['magik'].play()
                                display_nal(nextimage, boss_position, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                input_text = ''
                                continue

                            if cleaned_input == 'énigme1':
                                sound['magik'].play()
                                display_nal(nextimage, search_riddle1, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                input_text = ''
                                continue
                            
                            if cleaned_input == 'énigme2':
                                if search_spots >= 2:
                                    sound['magik'].play()
                                    display_nal(nextimage, search_riddle2, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue
                                else:
                                    sound['no_search_nnn_'].play()
                                    display_nal(nextimage, 'Nanapa jaipaltemps', '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue
                            
                            if cleaned_input == 'énigme3':
                                if search_spots >= 3:
                                    sound['magik'].play()
                                    display_nal(nextimage, search_riddle3, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue
                                else:
                                    sound['no_search_nnn_'].play()
                                    display_nal(nextimage, 'Nanapa jaipaltemps', '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue
                            
                            if cleaned_input == 'énigme4':
                                if search_spots >= 4:
                                    sound['magik'].play()
                                    display_nal(nextimage, search_riddle4, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue
                                else:
                                    sound['no_search_nnn_'].play()
                                    display_nal(nextimage, 'Nanapa jaipaltemps', '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue

                            if cleaned_input == 'énigme5':
                                if search_spots >= 5:
                                    sound['magik'].play()
                                    display_nal(nextimage, search_riddle5, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue
                                else:
                                    sound['no_search_nnn_'].play()
                                    display_nal(nextimage, 'Nanapa jaipaltemps', '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue
                            
                            elif cleaned_input == 'evy':
                                if not everest_mode:
                                    if everest_count > 0:
                                        enemy = 7
                                        conj_dict_gde_animal = conj_dicts_gde_animal[everest_count - 1]
                                        conj_dict_moy_animal = conj_dicts_moy_animal[everest_count - 1]
                                        conj_dict_pet_animal = conj_dicts_pet_animal[everest_count - 1]
                                        etext = etext_evy
                                        netext = netext_evy

                                        # Loop until the user succeeds
                                        while not special_animal(
                                            evytext, everest_mode, decoy, etext, netext, user_lives, 
                                            enemy_lives, enemy, enemy_alive, game_state.spot, game_state.orientation,
                                            nextimage, conj_dict_gde_animal, conj_dict_moy_animal, conj_dict_pet_animal, 
                                            sound_dict_animal, sound, display_nal, clean_input, WHITE_HEIGHT,
                                            k, ctrl_pressed, display_f_text, display_s_text
                                        ):
                                            pass  # Loop until the user succeeds
                                        
                                        everest_mode = True
                                        everest_count -= 1
                                        enemy = 0
                                        one = False  # Exit the loop once the challenge is completed
                                        break  # Exit the for loop

                                    else:
                                        sound['no_search_nnn_'].play()
                                        display_nal(nextimage, "Everest a trop combattu, elle est épuisée et doit maintenant se reposer jusqu'à la prochaine mission!", '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                        input_text = ''
                                        continue
                                
                                else:
                                    sound['no_search_nnn_'].play()
                                    display_nal(nextimage, "Everest est déjà prête au combat.", '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue

                            elif cleaned_input == decoy:
                                sound['tacos'].play()  # the end-of-level music, as when the level is won normally...
                                sound['cheat_ff_'].play()  # ...plus "full flemme" (cheat code)
                                all_running = False
                                one = False
                                return
                            
                            elif cleaned_input == ff:
                                sound['cheat_ff_'].play()
                                                      
                            elif cleaned_input == 'fouiller':
                                # !!! Adjust, commenté pour mission 3, pas besoin
                                #defuse = not any(trap_challenge_conditions.values()) and not any(shield_challenge_conditions.values())
                                # !!! Adjust, commenté pour mission 3, pas besoin
                                if search_challenge_conditions.get((game_state.spot, game_state.orientation)) and search_counter != 0: #and defuse:
                                    # !!! ADJUST (give phrase x to this challenge)
                                    phrase_dict_moy_search = phrase_dicts_moy_search[search_counter - 1]
                                    index = search_index[(game_state.spot, game_state.orientation)]
                                    search_text_init_curr = init_search_text_list[index]
                                    search_text_curr = search_text_list[index]
                                    item_curr = item_list[index]
                                    fake1item_curr = fake1item_list[index]
                                    fake2item_curr = fake2item_list[index]
                                    activate_item_list[index] = True

                                    if not special_searchoff(search_spots, search_riddle1, search_riddle2, search_riddle3, search_riddle4, search_riddle5,
                                                          item_curr, fake1item_curr, fake2item_curr, search_text_init_curr, search_text_curr, edoc, game_state.spot, game_state.orientation, nextimage, 
                                                          phrase_dict_moy_search, sound, display_nal, search_challenge_conditions, 
                                                          clean_input, decoy, WHITE_HEIGHT, enemy_lives, user_lives, enemy, 
                                                          enemy_alive, k, ctrl_pressed, display_w_text):
                                        game_state.spot = game_state.spot
                                        game_state.orientation = game_state.orientation
                                    
                                    else:
                                        search_counter -= 1
                                        for state, i in search_index.items():  # every view of this place is done
                                            if i == index:
                                                search_challenge_conditions[state] = False
                                        activate_item_list[index] = False
                                        with open('files/saves/save.txt', 'a') as file:
                                            file.write(f'search {game_state.spot}_{game_state.orientation}\n')                               
                                        
                                        if search_counter == 0:
                                            with open('files/saves/save.txt', 'a') as file:
                                                file.write('491\n')
                                            objective1 = True

                                        one = False
                                        break
                                
                                else:
                                    sound['no_search_nnn_'].play()
                                    display_nal(nextimage, "Il n'y a rien à chercher ici.", '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                    input_text = ''
                                    continue

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

                    elif event.key in (K_d, K_a, K_s, K_w, K_UP, K_DOWN, K_LEFT, K_RIGHT):
                        input_text = input_text

                    elif event.key == K_ESCAPE:
                        map_state['on'] = False
                    
                    else:
                        input_text += event.unicode
                    
                    if map_state['on'] and event.key in (K_d, K_a, K_s, K_w, K_UP, K_DOWN, K_LEFT, K_RIGHT):
                        pass  # the city map is open: the player doesn't move (close it with 'city'/'ville' or Escape)

                    elif event.key in (K_d, K_RIGHT):
                        sound['rotation_swoosh_'].play()
                        game_state.turn_right()
                        nextimage = images[f"{game_state.spot}_{game_state.orientation}"]

                    elif event.key in (K_a, K_LEFT):
                        sound['rotation_swoosh_'].play()
                        game_state.turn_left()
                        nextimage = images[f"{game_state.spot}_{game_state.orientation}"]

                    elif event.key in (K_s, K_DOWN):
                        sound['rotation_swoosh_'].play()
                        game_state.u_turn()
                        nextimage = images[f"{game_state.spot}_{game_state.orientation}"]

                    elif event.key in (K_w, K_UP):
                        previous_spot = game_state.spot
                        previous_orientation = game_state.orientation
                        game_state.go_straight()

                        if not (game_state.spot in shield_challenge_spots and shield_challenge_conditions[game_state.spot]):
                            nextimage = images[f"{game_state.spot}_{game_state.orientation}"]

                        if game_state.spot == previous_spot:
                            sound['no_movement_'].play()
                            if map_state['on']:
                                display_city('')
                            else:
                                display_nal(nextimage, "Mouvement impossible.", '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                            input_text = ''
                            continue  # Keep capturing key events for the next command
                        else:
                            sound['walk_'].play()
                    
                    if game_state.spot in trap_challenge_spots and trap_challenge_conditions[game_state.spot]:
                        # !!! ADJUST (give phrase x to this challenge)
                        while not special_trap(game_state.spot, nextimage, phrase_dict_moy_trap1, sound, display_nal, 
                                                trap_challenge_conditions, clean_input, decoy, WHITE_HEIGHT, enemy_lives, 
                                                user_lives, enemy, enemy_alive, k, ctrl_pressed, display_w_text):
                            pass  # Loop until the user succeeds
                        one = False
                        break

                    elif (game_state.spot, game_state.orientation) in enemy_challenge_conditions and enemy_challenge_conditions[(game_state.spot, game_state.orientation)]:
                        if enemy_counter != 0:

                            # Dice dict
                            enemy = enemies_list[enemy_counter - 1]
                            phrase_dict_gde = phrase_dicts_gde_enemy[enemy_counter - 1]
                            phrase_dict_moy = phrase_dicts_moy_enemy[enemy_counter - 1]
                            phrase_dict_pet = phrase_dicts_pet_enemy[enemy_counter - 1]
                            sound_dict = sound_dicts_enemy[enemy_counter - 1]
                            etext = enemies_text[enemy_counter - 1]
                            netext = 'none'

                            # Loop until the user succeeds
                            while not special_enemy(
                                evytext, everest_mode, decoy, etext, netext, user_lives, enemy_lives, enemy, enemy_alive, 
                                game_state.spot, game_state.orientation, nextimage, phrase_dict_gde, phrase_dict_moy, 
                                phrase_dict_pet, sound_dict, sound, display_nal, enemy_challenge_conditions, clean_input, 
                                WHITE_HEIGHT, k, ctrl_pressed, display_f_text, display_s_text
                            ):
                                pass  # Loop until the user succeeds
                            
                            everest_mode = False
                            enemy_challenge_conditions[(game_state.spot, game_state.orientation)] = False
                            with open('files/saves/save.txt', 'a') as file:
                                file.write(f'{enemy}\n')

                            enemy_counter -= 1
                            if enemy_counter == 0:
                                with open('files/saves/save.txt', 'a') as file:
                                    file.write('512\n')
                                objective2 = True

                            one = False  # Exit the loop once the challenge is completed
                            break  # Exit the for loop
                    
                    elif (game_state.spot, game_state.orientation) in boss_challenge_conditions and boss_challenge_conditions[(game_state.spot, game_state.orientation)] and objective1 and objective2:
                        # Loop until the user succeeds
                        sound_dict = sound_dict_boss
                        enemy = boss
                        etext = boss_text
                        netext = die_text

                        while not special_enemy(
                            evytext, everest_mode, decoy, etext, netext, user_lives, boss_lives, enemy, 
                            enemy_alive, game_state.spot, game_state.orientation,
                            nextimage, phrase_dict_gde_boss, phrase_dict_moy_boss, 
                            phrase_dict_pet_boss, sound_dict, sound,
                            display_nal, boss_challenge_conditions, clean_input, WHITE_HEIGHT,
                            k, ctrl_pressed, display_f_text, display_s_text
                        ):
                            pass  # Loop until the user succeeds
                        
                        everest_mode = False
                        boss_lives = 3
                        etext = revive_text
                        netext = boss_netext

                        while not special_animal(
                            evytext, everest_mode, decoy, etext, netext, user_lives, boss_lives, 
                            enemy, enemy_alive, game_state.spot, game_state.orientation,
                            nextimage, conj_dict_gde_boss, conj_dict_moy_boss, conj_dict_pet_boss, 
                            sound_dict, sound, display_nal, clean_input, WHITE_HEIGHT,
                            k, ctrl_pressed, display_f_text, display_s_text
                        ):
                            pass  # Loop until the user succeeds
                        
                        with open('files/saves/save.txt', 'a') as file:
                            file.write('723\n')
                        objective3 = True
                        boss_challenge_conditions[(game_state.spot, game_state.orientation)] = False
                        one = False  # Exit the loop once the challenge is completed
                        break  # Exit the for loop


                    elif game_state.spot in shield_challenge_spots and shield_challenge_conditions[game_state.spot]:
                        # !!! ADJUST (give phrase x to this challenge)
                        if not special_shield(game_state.spot, nextimage, phrase_dict_moy_shield1, sound, 
                                                display_nal, shield_challenge_conditions, clean_input, decoy, 
                                                WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive, k, 
                                                ctrl_pressed, display_w_text):
                            # If failed, keep player at the same spot
                            game_state.spot = previous_spot
                            game_state.orientation = previous_orientation
                            input_text = ''
                        
                        else:
                            one = False
                            break

                    if map_state['on'] and not display_w_text:
                        display_city(input_text)

                    elif display_w_text:
                        wrong_words_str = ', '.join(wrong_words)
                        display_nal(nextimage, "Commande non reconnue. Tapez 'info' puis Entrée pour voir les commandes." + wrong_words_str, "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                
                    else:
                        display_nal(nextimage, text, "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

                    pygame.display.flip()
                
                elif event.type == KEYUP and ctrl_pressed and event.key == K_q:
                    quit_state['quit'] = True
                    all_running = False
                    return

                elif event.type == KEYUP and event.key in (K_LCTRL, K_RCTRL):
                    ctrl_pressed = False


    ## Intro Part

    # Start screen: picture + instructions (modulesu/intro_screen.py)
    intro_title = 'MISSION ULTIME – {quest_title}'
    intro_lines = [
        "Trouvez l'objet caché, battez les 3 ennemis, puis le chef. 'énigme1' donne l'énigme qui mène à l'objet ('énigme2' s'il y en a une deuxième).",
        '- Bouger avec les flèches du clavier ou W A S D (sans Entrée) : haut / W = avancer, gauche / A et droite / D = tourner, bas / S = demi-tour.',
        "- Tapez, puis Entrée : 'fouiller' (chercher ici), 'ennemi' et 'chef' (où sont-ils ?), 'ville' (plan de la ville), 'titre', 'quitter' (sauvegarde ; tapez 'go' dans le menu pour revenir).",
        "- Combats : Ctrl + 1, 2 ou 3 pour écouter une phrase, puis tapez '1.', '2.' ou '3.' et la phrase (pistolet -1, mitraillette -2, shotgun -3).",
        "- Conjugaison (pour charger Everest, et pour le chef, qui revient à la vie une fois) : Ctrl + 1, 2 ou 3 vous donne un verbe et un temps. Tapez le numéro de l'arme, puis le verbe conjugué avec : arme 1 = je et tu ('1. je suis tu es') ; arme 2 = je, tu, il/elle, nous ('2. je suis tu es il est nous sommes') ; arme 3 = je, tu, il/elle, nous, vous, ils/elles. La voix vous dit s'il faut il ou elle.",
        "- Everest la chienne : tapez 'evy' et réussissez une conjugaison pour la charger (3 fois par mission). Puis, devant un ennemi ou le chef, tapez 'e. attaque' pour la lâcher : elle le dévore d'une bouchée !",
        "- Mip-mip ! = numéro d'arme oublié. Bip-bip ! = le mot que vous venez de taper est faux (vérifié à chaque espace) : corrigez-le avant de continuer.",
        "- Tapez 'info' puis Entrée à tout moment pour voir les commandes.",
    ]
    intro_footer = 'Appuyez sur une touche pour commencer !'
    intro_title = intro_title.replace('{quest_title}', str(quest_title))
    show_intro(screen, load.get('lobby'), intro_title, intro_lines, intro_footer, WIDTH, HEIGHT)

    ## Main part

    # Main loop
    while all_running:
        main(decoy, edoc)

    if quit_state['quit']:
        return

    ## Pre-Outro Part

    ## Outro part

    # Final message display
    display_nal(load.get('finalu'), "Félicibravotation !!! Vous avez terminé la Mission Ultime de la 'Bataille Royale du Français', le premier Text-Based Game to Improve Your Writing Skills, co-developpé par Aichi Panchu et la Rascasse de l'Espace. Spéciale dédicace à PapyCat pour l'inspiration et, bien sûr, Robert le Phacochère, notre mascotte officielle. Et comme l'a bien dit notre indispensable collaborateur, ChatGPT: \"Nezourez pas le code c'est du caca !!!\"", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

    # Wait for quit event
    while True:
        pygame.init()
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                return

##### COMMENT WHEN FINISHED #####
#lvlu()