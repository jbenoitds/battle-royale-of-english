import pygame 
import sys
from pygame.locals import *
from modules3.voice import speak

## Special Search challenge
def special_searchon(item_curr, fake1item_curr, fake2item_curr, search_text_init, search_text, edoc, 
                     spot, orientation, nextimage, phrase, sound, display_nal, search_challenge_conditions, 
                     clean_input, decoy, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive, k, 
                     ctrl_pressed, display_w_text):
    input_text = ''
    wrong_words = []
    correct_words = []
    word_err = False
    flags = False
    flagi = ''

    blup_counter = 5
    display_blup_text = False

    pygame.mixer.init()
    sound['search_triggers_'].play()
    display_nal(nextimage, search_text, "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

    while (spot, orientation) in search_challenge_conditions and search_challenge_conditions[(spot,orientation)]:
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

                    if cleaned_input == phrase or cleaned_input == decoy:
                        if cleaned_input == phrase:
                            sound['search_success_'].play()
                            display_nal(nextimage, "Well done! In my crystal ball, I see... I see... that this object is now yours! It goes straight into your bag. Press any key to continue.", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
    
                        elif cleaned_input == decoy:
                            sound['search_success_'].play()  # same sound as a success...
                            sound['cheat_ff_'].play()  # ...plus "full flemme" (cheat code)
                            display_nal(nextimage, "Well done! In my crystal ball, I see... I see... that this object is now yours! It goes straight into your bag. Press any key to continue.", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                
                        while True:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == KEYDOWN:
                                    return True

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

                elif event.key == pygame.K_BACKQUOTE or event.key == pygame.K_CARET:  
                    input_text = input_text
                
                elif ctrl_pressed and event.key == k:
                    speak(f'"{phrase}"', 'en')
                    ctrl_pressed = False

                elif event.key == K_ESCAPE:
                    sound['search_esc_'].play()
                    input_text = ""
                    return False  # Player wants to exit this challenge without advancing to the next spot

                else:
                    input_text += event.unicode

                    if len(input_text) >= 2:
                            text_verif = input_text.replace('\u2019', "'").strip().lower().split()
                            len_text_verif = len(text_verif)
                    
                            if event.key == pygame.K_SPACE:
                                current_pp = phrase.split()
                                len_current_pp = len(current_pp)

                                for i in range(len_text_verif):
                                    if len_text_verif == i + 1:
                                        if len_text_verif > len_current_pp:
                                            if text_verif[i] != current_pp[len_current_pp - 1]:
                                                word_err = True
                                                flagi = text_verif[i]
                                                flags = True
                                            
                                            else:
                                                word_err = False

                                        else:    
                                            if i >= len(current_pp) or text_verif[i] != current_pp[i]:
                                                word_err = True
                                                flagi = text_verif[i]
                                                flags = True
                                            
                                            else:
                                                word_err = False


                if display_w_text:
                    wrong_words_str = ', '.join(wrong_words)
                    correct_words_str = ', '.join(correct_words)
                    display_nal(nextimage, "That's not quite it, but you're almost there. *** Wrong word(s): " + wrong_words_str + "; Correction: " + correct_words_str + " ***", "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                 
                    if word_err and blup_counter > 0:
                        display_nal(nextimage, f"!!! WATCH OUT !!! Wrong word: \"{flagi}\". \nRead it again: does it look right? Tips: their / there / they're; to / too / two; its / it's? Verb: past tense with -ed, or irregular (ran, ate, went)? Plural: -s or -es? Silent letters (knee, write, lamb)? Double letters (happy, running)?", "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)                    
                        if flags:
                            if blup_counter == 1:                             
                                display_blup_text = True
                                sound['blipblip'].play()
                                blup_counter -= 1
                                flags = False
                            else:
                                sound['blipblip'].play()
                                blup_counter -= 1
                                flags = False

                elif word_err and blup_counter > 0:
                    display_nal(nextimage, f"!!! WATCH OUT !!! Wrong word: \"{flagi}\". \nRead it again: does it look right? Tips: their / there / they're; to / too / two; its / it's? Verb: past tense with -ed, or irregular (ran, ate, went)? Plural: -s or -es? Silent letters (knee, write, lamb)? Double letters (happy, running)?", "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                    if flags:
                        if blup_counter == 1:                         
                            display_blup_text = True
                            sound['blipblip'].play()
                            blup_counter -= 1
                            flags = False
                        else:
                            sound['blipblip'].play()
                            blup_counter -= 1
                            flags = False

                else:
                    display_nal(nextimage, search_text, "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

                if display_blup_text:
                    display_nal(nextimage, "Careful, this is your last blup blup blup... after this, you can keep going, but without this precious help. Hang in there, you can do it!", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                    display_blup_text = False

                continue
                #pygame.display.flip()

            elif event.type == KEYUP:
                if event.key == K_LCTRL or event.key == K_RCTRL:
                    ctrl_pressed = False

    return False  # Challenge not triggered, keep player at the same spot