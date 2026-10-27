import pygame 
import sys
from pygame.locals import *
from modulesu.special_searchon import special_searchon


# Words the player can type to name an object (the object files have English names, e.g. 'bucket.png')
ITEM_WORDS = {'alarm clock': 'alarm_clock', 'clock radio': 'alarm_clock', 'batteries': 'battery', 'car keys': 'car_keys', 'car key': 'car_keys', 'pot': 'cauldron', 'corn cob': 'corn', 'keys': 'door_keys', 'door keys': 'door_keys', 'key': 'door_keys', 'gloves': 'gloves', 'glove': 'gloves', 'spell book': 'grimoire', 'magic book': 'grimoire', 'guitar': 'guitare', 'cowboy hat': 'hat', 'backpack': 'hiking_bag', 'hiking bag': 'hiking_bag', 'id card': 'id_card', 'lamp': 'lantern', 'old clock': 'old_clock', 'clock': 'old_clock', 'sneaker': 'shoe', 'sneakers': 'shoe', 'shoes': 'shoe', 'tomatoes': 'tomato', 'television': 'tv', 'tv set': 'tv', 'watch': 'wrist_watch', 'wrist watch': 'wrist_watch'}
ARTICLES = ['the ', 'an ', 'a ', 'some ']


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

    text_searchoff_init = "Well done, you found the right place... well, one of the right places. Now that I think about it, maybe you found the wrong right place, or the right wrong place, or the... Anyway, now remember the riddle of the GPT Master and choose the right object. Choose carefully, because any mistake will be punished BY DEATH !!! Uh no, by losing a few points."
    text_searchoff_false = "Oopsie, that's not the right object, or it wasn't spelled right. YOU LOST !!! Well, lost a few points, I mean. The right object was... actually I have no idea, that's the whole point of the game, remember? No? Oh well. Try another object, or go grab a snack or take a bathroom break, you do you."
    text_searchoff_very_false = "Hmm, I don't know what to tell you, this object is either not even here or really, really badly spelled! No, I'm kidding, maybe it's just a teeny bit misspelled? Why am I so mean? BECAUUUUUSE. No seriously, I apologize, I'm sorry. Still, that's not it... or it is and there's a bug (if so: 100 bonus points)!"

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
                    if cleaned_input.startswith('clue'):  # 'clue1'..'clue5' = same as 'riddle1'..'riddle5'
                        cleaned_input = 'riddle' + cleaned_input[4:]

                    if cleaned_input in [item_curr, fake1item_curr, fake2item_curr, 'riddle1', 'riddle2', 'riddle3', 'riddle4', 'riddle5']:
                        if cleaned_input == 'riddle1':
                            sound['magik'].play()
                            display_nal(nextimage, search_riddle1, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                            input_text = ''
                            continue
                        
                        elif cleaned_input == 'riddle2':
                            if search_spots >= 2:
                                sound['magik'].play()
                                display_nal(nextimage, search_riddle2, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                input_text = ''
                                continue
                            else:
                                sound['no_search_nnn_'].play()
                                display_nal(nextimage, "Nope, no time for that", '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                input_text = ''
                                continue
                        
                        elif cleaned_input == 'riddle3':
                            if search_spots >= 3:
                                sound['magik'].play()
                                display_nal(nextimage, search_riddle3, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                input_text = ''
                                continue
                            else:
                                sound['no_search_nnn_'].play()
                                display_nal(nextimage, "Nope, no time for that", '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                input_text = ''
                                continue
                        
                        elif cleaned_input == 'riddle4':
                            if search_spots >= 4:
                                sound['magik'].play()
                                display_nal(nextimage, search_riddle4, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                input_text = ''
                                continue
                            else:
                                sound['no_search_nnn_'].play()
                                display_nal(nextimage, "Nope, no time for that", '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                input_text = ''
                                continue

                        elif cleaned_input == 'riddle5':
                            if search_spots >= 5:
                                sound['magik'].play()
                                display_nal(nextimage, search_riddle5, '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                input_text = ''
                                continue
                            else:
                                sound['no_search_nnn_'].play()
                                display_nal(nextimage, "Nope, no time for that", '', WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
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