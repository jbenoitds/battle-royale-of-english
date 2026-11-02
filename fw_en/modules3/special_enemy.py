import pygame 
import sys
from pygame.locals import *
from modules3.voice import speak

## Special enemy challenge
def special_enemy(decoy, etext, user_lives, enemy_lives, enemy, enemy_alive, spot, orientation, nextimage, phrase_dict_gde, phrase_dict_moy, phrase_dict_pet, sound_dict, sound, display_nal, enemy_challenge_conditions, clean_input, WHITE_HEIGHT, k, ctrl_pressed, display_f_text, display_s_text):
    input_text = ''
    wrong_words = []
    correct_words = []
    word_err = False
    flags = False
    flagi = ''
    
    counter2 = 1
    count_gde = 1
    count_moy = 1
    count_pet = 1

    pygame.mixer.init()

    sound_dict[f'{enemy}4'].play()
    display_nal(nextimage, etext, "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

    while (spot, orientation) in enemy_challenge_conditions and enemy_challenge_conditions[(spot, orientation)]:
        # Iterating through phrase dictionaries
        counter2key = f'phrase{counter2}'
        ### !!! GENERALIZE 4
        if counter2 < 4:
            current_phrase_gde = phrase_dict_gde[counter2key]
            current_phrase_moy = phrase_dict_moy[counter2key]
            current_phrase_pet = phrase_dict_pet[counter2key]
            
            for event in pygame.event.get():
                
                display_s_text = False

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                            
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        word_err = False  # a new try: forget the old warning
                        flags = False
                        cleaned_input = clean_input(input_text)

                        category = cleaned_input[:2]
                        cleaned_input = cleaned_input[2:]
                        cleaned_input = clean_input(cleaned_input)

                        words_user = cleaned_input.split()
                        wrong_words = []
                        correct_words = []
                        display_f_text = False

                        if category == "1.":
                            if count_pet <= 2:
                                count_pet += 1
                            
                                if cleaned_input.split() == current_phrase_pet.split() or cleaned_input == decoy:
                                    input_text = ''
                                    sound['gun'].play()
                                    if cleaned_input == decoy:
                                        sound['cheat_ff_'].play()  # cheat code: "full flemme" on top of the weapon sound
                                    ### ADJUSTED FOR INSTANT KILL GDE
                                    enemy_lives -= 1  # Decrease enemy life
                                    counter2 += 1

                                    if enemy_lives <= 0:
                                        sound_dict[f'{enemy}3'].play()
                                        # Display next image
                                        if enemy == 7:
                                            display_nal(nextimage, "Ahhhh, nothing beats a nice ice-cold Nuka-Cola, especially one you just took from a knocked-out Kakachi. That'll teach you, you rascal!", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                        else:
                                            display_nal(nextimage, "The sun is dead, it's dead. We'll never hear cock-a-doodle-doo again, not even when it cock-a-doodle-did. Press any key to continue, after a few seconds of silence in its memory, or not, it's up to you.", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                        
                                        pygame.display.flip()

                                        # Wait for key press to end challenge
                                        # continue instead
                                        wait_for_keypress = True
                                        while wait_for_keypress:
                                            for event in pygame.event.get():
                                                if event.type == KEYDOWN:
                                                    wait_for_keypress = False

                                        enemy_challenge_conditions[(spot, orientation)] = False
                                        return True  # Successfully defeated the enemy
                                    
                                    else:
                                        sound_dict[f'{enemy}2'].play()

                                    display_s_text = True
                                    input_text = ''
                            
                                elif cleaned_input == decoy:
                                    sound['cheat_ff_'].play()
                                    enemy_challenge_conditions[(spot, orientation)] = False
                                    return True  # Successfully wrote the phrase
                                
                                else:
                                    for user_word, correct_word in zip(words_user, current_phrase_pet.split()):
                                        if user_word != correct_word:
                                            wrong_words.append(user_word)
                                            correct_words.append(correct_word)
                                    sound_dict[f'{enemy}1'].play()
                                    user_lives -= 1  # Decrease user life
                                    if user_lives == 0:
                                        ### !!! ADD SOUND
                                        return False  # User failed the challenge
                                    display_f_text = True
                                    input_text = ''

                            else:
                                sound['surprise_'].play()
                                # Display next image
                                display_nal(nextimage, "You have no short sentences left to three-shoot your opponent. Try a medium or long sentence instead, if you have any left.", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                input_text = ''
                                continue

                        elif category == "2.":
                            if count_moy <= 100:
                                count_moy += 1
                            
                                if cleaned_input.split() == current_phrase_moy.split() or cleaned_input == decoy:
                                    input_text = ''
                                    sound['rifle'].play()  
                                    if cleaned_input == decoy:
                                        sound['cheat_ff_'].play()  # cheat code: "full flemme" on top of the weapon sound
                                    ### ADJUSTED FOR INSTANT KILL GDE
                                    enemy_lives -= 2  # Decrease enemy life
                                    counter2 += 1

                                    if enemy_lives <= 0:
                                        sound_dict[f'{enemy}3'].play()
                                        # Display next image
                                        if enemy == 7:
                                            display_nal(nextimage, "Ahhhh, nothing beats a nice ice-cold Nuka-Cola, especially one you just took from a knocked-out Kakachi. That'll teach you, you rascal!", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                        else:
                                            display_nal(nextimage, "The sun is dead, it's dead. We'll never hear cock-a-doodle-doo again, not even when it cock-a-doodle-did. Press any key to continue, after a few seconds of silence in its memory, or not, it's up to you.", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                        pygame.display.flip()

                                        # Wait for key press to end challenge
                                        # continue instead
                                        wait_for_keypress = True
                                        while wait_for_keypress:
                                            for event in pygame.event.get():
                                                if event.type == KEYDOWN:
                                                    wait_for_keypress = False

                                        enemy_challenge_conditions[(spot, orientation)] = False
                                        return True  # Successfully defeated the enemy
                                    
                                    else:                                    
                                        sound_dict[f'{enemy}2'].play()

                                    display_s_text = True
                                    input_text = ''
                            
                                elif cleaned_input == decoy:
                                    sound['cheat_ff_'].play()
                                    enemy_challenge_conditions[(spot, orientation)] = False
                                    return True  # Successfully wrote the phrase
                                
                                else:
                                    for user_word, correct_word in zip(words_user, current_phrase_moy.split()):
                                        if user_word != correct_word:
                                            wrong_words.append(user_word)
                                            correct_words.append(correct_word)
                                    sound_dict[f'{enemy}1'].play()
                                    user_lives -= 1  # Decrease user life
                                    if user_lives == 0:
                                        ### !!! ADD SOUND
                                        return False  # User failed the challenge
                                    display_f_text = True
                                    input_text = ''

                            else:
                                sound['surprise_'].play()
                                # Display next image
                                display_nal(nextimage, "You have no medium sentences left to two-shoot your opponent. Try a long or short sentence instead, if you have any left.", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                input_text = ''
                                continue

                        elif category == "3.":
                            if count_gde <= 1:
                                count_gde += 1
                            
                                if cleaned_input.split() == current_phrase_gde.split() or cleaned_input == decoy:
                                    sound['shotgun'].play()
                                    if cleaned_input == decoy:
                                        sound['cheat_ff_'].play()  # cheat code: "full flemme" on top of the weapon sound
                                    input_text = ''
                                    ### ADJUSTED FOR INSTANT KILL GDE
                                    enemy_lives -= 3  # Decrease enemy life
                                    counter2 += 1
                                    if enemy_lives <= 0:
                                        sound_dict[f'{enemy}3'].play()
                                        # Display next image
                                        if enemy == 7:
                                            display_nal(nextimage, "Ahhhh, nothing beats a nice ice-cold Nuka-Cola, especially one you just took from a knocked-out Kakachi. That'll teach you, you rascal!", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                        else:
                                            display_nal(nextimage, "The sun is dead, it's dead. We'll never hear cock-a-doodle-doo again, not even when it cock-a-doodle-did. Press any key to continue, after a few seconds of silence in its memory, or not, it's up to you.", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                        pygame.display.flip()

                                        # Wait for key press to end challenge
                                        # continue instead
                                        wait_for_keypress = True
                                        while wait_for_keypress:
                                            for event in pygame.event.get():
                                                if event.type == KEYDOWN:
                                                    wait_for_keypress = False

                                        enemy_challenge_conditions[(spot, orientation)] = False
                                        return True  # Successfully defeated the enemy
                                    else:                                                                              
                                        sound_dict[f'{enemy}2'].play()

                                    display_s_text = True
                                    input_text = ''
                            
                                elif cleaned_input == decoy:
                                    sound['cheat_ff_'].play()
                                    enemy_challenge_conditions[(spot, orientation)] = False
                                    return True  # Successfully wrote the phrase
                                
                                else:
                                    for user_word, correct_word in zip(words_user, current_phrase_gde.split()):
                                        if user_word != correct_word:
                                            wrong_words.append(user_word)
                                            correct_words.append(correct_word)
                                    sound_dict[f'{enemy}1'].play()
                                    user_lives -= 1  # Decrease user life
                                    if user_lives == 0:
                                        ### !!! ADD SOUND
                                        return False  # User failed the challenge
                                    display_f_text = True
                                    input_text = ''

                            else:
                                sound['surprise_'].play()
                                # Display next image
                                display_nal(nextimage, "You have no long sentences left to one-shoot your opponent. Try a medium or short sentence instead, if you have any left.", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                input_text = ''
                                continue

                        else:
                            sound['surprise_'].play()
                            # Display next image
                            display_nal(nextimage, "Number not recognized. Try again, and don't forget to type \"1.\", \"2.\" or \"3.\" before your sentence.", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                            input_text = ''
                            continue
                    
                    elif event.key == K_BACKSPACE:
                        input_text = input_text[:-1]
                        word_err = False  # correcting: the warning goes away until the next space

                    elif event.key == K_LCTRL or event.key == K_RCTRL:
                        ctrl_pressed = True
                    
                    elif ctrl_pressed and event.key == K_1:
                        speak(f'"{current_phrase_pet}"', 'en')
                        ctrl_pressed = False

                    elif ctrl_pressed and event.key == K_2:
                        speak(f'"{current_phrase_moy}"', 'en')
                        ctrl_pressed = False

                    elif ctrl_pressed and event.key == K_3:
                        speak(f'"{current_phrase_gde}"', 'en')
                        ctrl_pressed = False

                    elif event.key == pygame.K_BACKQUOTE or event.key == pygame.K_CARET:  
                        input_text = input_text

                    else:
                        input_text += event.unicode

                        
                        if len(input_text) >= 2:
                            cat_verif = input_text[:2].strip().lower()
                            text_verif = input_text[2:].replace('\u2019', "'").strip().lower().split()
                            len_text_verif = len(text_verif)
                            
                            if cat_verif not in ["1.","2.","3."]:
                                sound['mipmip'].play()
                                display_nal(nextimage, "*** !!! WATCH OUT !!! You forgot to choose your weapon with \"1.\", \"2.\" or \"3.\" !!! WATCH OUT !!! ***", "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                                continue

                            elif cat_verif == '1.':
                                if event.key == pygame.K_SPACE:
                                    current_pp = current_phrase_pet.split()

                                    for i in range(len_text_verif):
                                        if len_text_verif == i + 1:
                                            if i >= len(current_pp) or text_verif[i] != current_pp[i]:
                                                word_err = True
                                                flagi = text_verif[i]
                                                flags = True
                                            
                                            else:
                                                word_err = False

                            elif cat_verif == '2.':
                                if event.key == pygame.K_SPACE:
                                    current_pp = current_phrase_moy.split()

                                    for i in range(len_text_verif):
                                        if len_text_verif == i + 1:
                                            if i >= len(current_pp) or text_verif[i] != current_pp[i]:
                                                word_err = True
                                                flagi = text_verif[i]
                                                flags = True
                                            
                                            else:
                                                word_err = False

                            elif cat_verif == '3.':
                                if event.key == pygame.K_SPACE:
                                    current_pp = current_phrase_gde.split()

                                    for i in range(len_text_verif):
                                        if len_text_verif == i + 1:
                                            if i >= len(current_pp) or text_verif[i] != current_pp[i]:
                                                word_err = True
                                                flagi = text_verif[i]
                                                flags = True
                                            
                                            else:
                                                word_err = False

                    if display_f_text:
                        wrong_words_str = ', '.join(wrong_words)
                        correct_words_str = ', '.join(correct_words)
                        display_nal(nextimage, "That's not quite it, but you're almost there. You take a hit right in the face, but you recover instantly, thanks to the power of the Funk... the Funk. *** Wrong word(s): " + wrong_words_str + "; Correction: " + correct_words_str + " ***", "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                        
                        if word_err:
                            display_nal(nextimage, f"!!! WATCH OUT !!! Wrong word: \"{flagi}\". \nRead it again: does it look right? Tips: their / there / they're; to / too / two; its / it's? Verb: past tense with -ed, or irregular (ran, ate, went)? Plural: -s or -es? Silent letters (knee, write, lamb)? Double letters (happy, running)?", "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)                    
                            if flags:
                                sound['blipblip'].play()
                                flags = False

                    elif display_s_text:
                        display_nal(nextimage, "Well done, your enemy just took a hit, keep it up! Not so tough now, are you, rascal! Not bragging anymore... watch out, it's getting back up! Here we go again.", "", WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                        
                    elif word_err:
                        display_nal(nextimage, f"!!! WATCH OUT !!! Wrong word: \"{flagi}\". \nRead it again: does it look right? Tips: their / there / they're; to / too / two; its / it's? Verb: past tense with -ed, or irregular (ran, ate, went)? Plural: -s or -es? Silent letters (knee, write, lamb)? Double letters (happy, running)?", "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)
                        if flags:
                            sound['blipblip'].play()
                            flags = False

                    else:
                        display_nal(nextimage, etext, "" + input_text, WHITE_HEIGHT, enemy_lives, user_lives, enemy, enemy_alive)

                    continue
                    #pygame.display.flip()
                
                elif event.type == KEYUP:
                    if event.key == K_LCTRL or event.key == K_RCTRL:
                        ctrl_pressed = False

    return False  # Challenge failed, keep player at the same spot