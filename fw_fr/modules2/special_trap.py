import pygame 
import sys
from pygame.locals import *
from modules3.voice import speak

## Special Trap challenge
def special_trap(spot, nextimage, phrase, phraseg, sound, display_nal, trap_challenge_conditions, clean_input, cheat, WHITE_HEIGHT, k, ctrl_pressed, display_w_text):
    input_text = ''
    wrong_words = []
    correct_words = []
    word_err = False
    flags = False
    flagi = ''

    pygame.mixer.init()
    sound['trap_triggers_'].play()
    display_nal(nextimage, "Un piège s'est refermé sur vos jambes, vous bloquant complètement! Écoutez la phrase avec \"Ctrl + 1\" puis tapez la correctement pour en sortir.", "" + input_text, WHITE_HEIGHT)

    while trap_challenge_conditions[spot]:
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
                        sound['trap_success_'].play()
                        trap_challenge_conditions[spot] = False
                        return True  # Successfully wrote the phrase
                    
                    elif cleaned_input == cheat:
                        sound['trap_success_'].play()  # same sound as a success...
                        sound['cheat_ff_'].play()  # ...plus "full flemme" (cheat code)
                        trap_challenge_conditions[spot] = False
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
                    speak(phraseg, 'fr')
                    ctrl_pressed = False

                elif event.key == pygame.K_BACKQUOTE or event.key == pygame.K_CARET:  
                    input_text = input_text

                else:
                    input_text += event.unicode

                    text_verif = input_text.replace('\u2019', "'").strip().lower().split()
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
                    display_nal(nextimage, "Ce n'est pas tout à fait ça, mais vous y êtes presque. *** Mot(s) erroné(s): " + wrong_words_str + "; Correction: " + correct_words_str + " ***", "" + input_text, WHITE_HEIGHT)
                   
                    if word_err:
                        display_nal(nextimage, f"!!! ATTENTION !!! Mot incorrect: \"{flagi}\". \nLisez-le, est-ce qu'il sonne bien? Règles: 'à / avait'; 'mordre / mordu; 'son' (le sien) / 'sont' (verbe)'? Verbe: conjugué? Accord: masculin / féminin; singulier / pluriel? Lettres muettes à la fin; sons plusieurs écritures, comme 'o' / 'eau'.", "" + input_text, WHITE_HEIGHT)                    
                        if flags:
                            sound['blipblip'].play()
                            flags = False

                elif word_err:
                        display_nal(nextimage, f"!!! ATTENTION !!! Mot incorrect: \"{flagi}\". \nLisez-le, est-ce qu'il sonne bien? Règles: 'à / avait'; 'mordre / mordu; 'son' (le sien) / 'sont' (verbe)'? Verbe: conjugué? Accord: masculin / féminin; singulier / pluriel? Lettres muettes à la fin; sons plusieurs écritures, comme 'o' / 'eau'.", "" + input_text, WHITE_HEIGHT)                    
                        if flags:
                            sound['blipblip'].play()
                            flags = False

                else:
                    display_nal(nextimage, "Un piège s'est refermé sur vos jambes, vous bloquant complètement! Écoutez la phrase avec \"Ctrl + 1\" puis tapez la correctement pour en sortir.", "" + input_text, WHITE_HEIGHT)

                pygame.display.flip()
            
            elif event.type == KEYUP:
                if event.key == K_LCTRL or event.key == K_RCTRL:
                    ctrl_pressed = False

    return False  # Challenge failed, keep player at the same spot