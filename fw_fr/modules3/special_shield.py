import pygame 
import sys
from pygame.locals import *
from modules3.voice import speak

## Special Shield room challenge
def special_shield(spot, nextimage, phrase, sound, display_nal, shield_challenge_conditions, clean_input, decoy, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive, k, ctrl_pressed, display_w_text):
    input_text = ''
    wrong_words = []
    correct_words = []
    word_err = False
    flags = False
    flagi = ''

    pygame.mixer.init()
    sound['shield_triggers_'].play()
    display_nal(nextimage, "Vous ne pouvez pas vous rendre à cet endroit, il semble qu'il soit protégé par une barrière d'énergie! Écoutez la phrase avec \"Ctrl + 1\" puis tapez la correctement pour la désactiver.", "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

    while shield_challenge_conditions[spot]:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                        
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    word_err = False  # a new try: forget the old warning
                    flags = False
                    cleaned_input = clean_input(input_text)
                    words_user = cleaned_input.split()
                    wrong_words = []
                    correct_words = []

                    if cleaned_input == phrase:
                        sound['shield_success_'].play()
                        shield_challenge_conditions[spot] = False
                        return True  # Successfully wrote the phrase
                    
                    if cleaned_input == decoy:
                        sound['shield_success_'].play()  # same sound as a success...
                        sound['cheat_ff_'].play()  # ...plus "full flemme" (cheat code)
                        shield_challenge_conditions[spot] = False
                        return True  # Successfully wrote the phrase
                                        
                    else:
                        for user_word, correct_word in zip(words_user, phrase.split()):
                            if user_word != correct_word:
                                wrong_words.append(user_word)
                                correct_words.append(correct_word)
                        sound['failed_chall_'].play()
                        display_w_text = True
                        input_text = ''
                
                elif event.key == K_BACKSPACE:
                    input_text = input_text[:-1]
                    word_err = False  # correcting: the warning goes away until the next space

                elif event.key == K_LCTRL or event.key == K_RCTRL:
                    ctrl_pressed = True
                
                elif ctrl_pressed and event.key == k:
                    speak(f'"{phrase}"', 'fr')
                    ctrl_pressed = False
                
                elif event.key == pygame.K_BACKQUOTE or event.key == pygame.K_CARET:  
                    input_text = input_text

                elif event.key == K_ESCAPE:
                    sound['shield_esc_'].play()
                    input_text = ""
                    return False  # Player wants to exit this challenge without advancing to the next spot

                else:
                    input_text += event.unicode

                    if len(input_text) >= 2:
                            text_verif = input_text[2:].replace('\u2019', "'").strip().lower().split()
                            len_text_verif = len(text_verif)
                    
                            if event.key == pygame.K_SPACE:
                                current_pp = phrase.split()

                                for i in range(len_text_verif):
                                    if len_text_verif == i + 1:
                                        if i >= len(current_pp) or text_verif[i] != current_pp[i]:
                                            word_err = True
                                            flagi = text_verif[i]
                                            flags = True
                                        
                                        else:
                                            word_err = False
                

                if display_w_text:
                    wrong_words_str = ', '.join(wrong_words)
                    correct_words_str = ', '.join(correct_words)
                    display_nal(nextimage, "Ce n'est pas tout à fait ça, mais vous y êtes presque. *** Mot(s) erroné(s): " + wrong_words_str + "; Correction: " + correct_words_str + " ***", "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                  
                    if word_err:
                        display_nal(nextimage, f"!!! ATTENTION !!! Mot incorrect: \"{flagi}\". \nLisez-le, est-ce qu'il sonne bien? Règles: 'à / avait'; 'mordre / mordu; 'son' (le sien) / 'sont' (verbe)'? Verbe: conjugué? Accord: masculin / féminin; singulier / pluriel? Lettres muettes à la fin; sons plusieurs écritures, comme 'o' / 'eau'.", "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)                    
                        if flags:
                            sound['blipblip'].play()
                            flags = False

                elif word_err:
                        display_nal(nextimage, f"!!! ATTENTION !!! Mot incorrect: \"{flagi}\". \nLisez-le, est-ce qu'il sonne bien? Règles: 'à / avait'; 'mordre / mordu; 'son' (le sien) / 'sont' (verbe)'? Verbe: conjugué? Accord: masculin / féminin; singulier / pluriel? Lettres muettes à la fin; sons plusieurs écritures, comme 'o' / 'eau'.", "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)                    
                        if flags:
                            sound['blipblip'].play()
                            flags = False

                else:
                    display_nal(nextimage, "Vous ne pouvez pas vous rendre à cet endroit, il semble qu'il soit protégé par une barrière d'énergie! Écoutez la phrase avec \"Ctrl + 1\" puis tapez la correctement pour la désactiver.", "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

                pygame.display.flip()
            
            elif event.type == KEYUP:
                if event.key == K_LCTRL or event.key == K_RCTRL:
                    ctrl_pressed = False

    return False  # Challenge failed, keep player at the same spot