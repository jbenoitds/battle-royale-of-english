import pygame 
import sys
from pygame.locals import *
from modulesu.special_searchon import special_searchon


# Words the player can type to name an object (the object files have English names, e.g. 'bucket.png')
ITEM_WORDS = {'réveil': 'alarm_clock', 'réveille-matin': 'alarm_clock', 'banane': 'banana', 'pile': 'battery', 'piles': 'battery', 'balai': 'broom', 'seau': 'bucket', 'clés de voiture': 'car_keys', 'clé de voiture': 'car_keys', 'chaudron': 'cauldron', 'marmite': 'cauldron', 'boussole': 'compass', 'maïs': 'corn', 'épi de maïs': 'corn', 'clés': 'door_keys', 'trousseau de clés': 'door_keys', 'gomme': 'eraser', 'gomme à effacer': 'eraser', 'gants': 'gloves', 'grimoire': 'grimoire', 'livre de magie': 'grimoire', 'guitare': 'guitare', 'marteau': 'hammer', 'chapeau': 'hat', 'chapeau de cowboy': 'hat', 'sac à dos': 'hiking_bag', "carte d'identité": 'id_card', 'couteau': 'knife', 'lanterne': 'lantern', 'lampe': 'lantern', 'briquet': 'lighter', 'carte': 'map', 'plan': 'map', 'horloge': 'old_clock', 'vieille horloge': 'old_clock', 'crayon': 'pencil', 'piano': 'piano', 'télécommande': 'remote', 'règle': 'ruler', 'tournevis': 'screwdriver', 'soulier': 'shoe', 'chaussure': 'shoe', 'espadrille': 'shoe', 'basket': 'shoe', 'éponge': 'sponge', 'tomate': 'tomato', 'torche': 'torch', 'flambeau': 'torch', 'télé': 'tv', 'télévision': 'tv', 'violon': 'violin', 'sorcière': 'witch', 'montre': 'wrist_watch'}
ARTICLES = ['les ', 'le ', 'la ', "l'", 'un ', 'une ', 'des ', 'du ']


def item_word(text):
    """'le seau' / 'un seau' / 'seau' -> 'bucket' (unknown words are returned unchanged)."""
    t = ' '.join(text.replace('\u2019', "'").split())
    for art in ARTICLES:
        if t.startswith(art):
            t = t[len(art):]
            break
    return ITEM_WORDS.get(t, t.replace(' ', '_') if t.replace(' ', '_') in ITEM_WORDS.values() else t)

## Special searchoff
def special_searchoff(search_spots, search_riddle1, search_riddle2, search_riddle3, search_riddle4, search_riddle5,     
                      item_curr, fake1item_curr, fake2item_curr, search_text_init_curr, search_text_curr, edoc, spot, 
                      orientation, nextimage, phrase_dict_moy_search, sound, display_nal, search_challenge_conditions, 
                      clean_input, decoy, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive, k, ctrl_pressed, 
                      display_w_text):
    input_text = ''
    pygame.mixer.init()

    phrase_counter = 1
    phrases_list = list(phrase_dict_moy_search.values())
    phrase_moy_search = phrases_list[phrase_counter - 1]

    text_searchoff_init = "Bravo, vous avez trouvé le bon endroit... enfin, l'un des bons endroits. Maintenant que j'y pense, vous avez peut-être trouvé le mauvais bon endroit, ou le bon mauvais endroit, ou le... Bref, à présent, rappelez vous de l'énigme du GPTère Fourras et choisissez le bon objet. Choisissez bien, car toute erreur sera punie DE MORT !!! Euh non, de quelques points en moins."
    text_searchoff_false = "Oh la boulette, ce n'est pas le bon objet, ou il n'a pas été bien écrit. VOUS AVEZ PERDU !!! Enfin, perdu quelques points quoi. Le bon objet était... j'en sais rien en fait, c'est le principe du jeu, vous vous rappelez? Non? Ah, tant pis. Tentez un autre objet, ou allez manger un morceau ou faites une pause pipi, vous faites ce que vous voulez après tout."
    text_searchoff_very_false = "Ah, là je sais pas quoi vous dire, cet objet est soit même pas là soit vraiment très mal écrit! Non, je plaisante, si ça se trouve il est juste un tout petit peu mal écrit? Pourquoi suis-je aussi méchant? PARCE QUEEEEEEE. Non sérieux, je m'excuse, je suis désolé. N'empêche c'est pas ça... ou alors c'est ça et il y a un bug (si c'est le cas: 100 pts en plus)!"

    display_nal(nextimage, search_text_init_curr, "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

    while search_challenge_conditions[(spot, orientation)]:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                        
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    cleaned_input = clean_input(input_text)
                    cleaned_input = item_word(cleaned_input)

                    if cleaned_input in [item_curr, fake1item_curr, fake2item_curr, 'énigme1', 'énigme2', 'énigme3', 'énigme4', 'énigme5']:
                        if cleaned_input == 'énigme1':
                            sound['magik'].play()
                            display_nal(nextimage, search_riddle1, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                            input_text = ''
                            continue
                        
                        elif cleaned_input == 'énigme2':
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
                        
                        elif cleaned_input == 'énigme3':
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
                        
                        elif cleaned_input == 'énigme4':
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

                        elif cleaned_input == 'énigme5':
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
                        
                        if cleaned_input == item_curr:
                            
                            # Loop until the user succeeds
                            while not special_searchon(
                                item_curr, fake1item_curr, fake2item_curr, search_text_init_curr, 
                                search_text_curr, edoc, spot, orientation, nextimage, 
                                phrase_moy_search, sound, display_nal, search_challenge_conditions, 
                                clean_input, decoy, WHITE_HEIGHT, enemy_lives, user_lives, enemy, 
                                enemy_alive, k, ctrl_pressed, display_w_text
                            ):
                                pass  # Loop until the user succeeds
                        
                            return True
                        
                        elif cleaned_input == fake1item_curr:
                            sound['no_search_nnn_'].play()
                            display_nal(nextimage, text_searchoff_false, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                            input_text = ''
                            continue


                        elif cleaned_input == fake2item_curr:
                            sound['no_search_nnn_'].play()
                            display_nal(nextimage, text_searchoff_false, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                            input_text = ''
                            continue
                                                   
                        
                    else:
                        sound['no_search_nnn_'].play()
                        display_nal(nextimage, text_searchoff_very_false, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                        input_text = ''
                        continue
                
                elif event.key == K_BACKSPACE:
                    input_text = input_text[:-1]

                elif event.key == pygame.K_BACKQUOTE or event.key == pygame.K_CARET:  
                    input_text = input_text

                else:
                    input_text += event.unicode
                                    
                display_nal(nextimage, search_text_init_curr, "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

                pygame.display.flip()
                

    return False  # Challenge failed, keep player at the same spot