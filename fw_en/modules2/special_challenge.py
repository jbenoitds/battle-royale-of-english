# type: ignore
## Special Shield room challenge
def special_challenge(spot, escape):
    global screen, nextimage, all_running, ctrl_pressed, cheat, phrase1, phrase2, display_w_text, k
    input_text = ''
    display_w_text = False
    wrong_words = []
    correct_words = []
    phrase = phrase2
    phraseg = phrase2g

    sound['shield_triggers_'].play()
    display_nal(nextimage, "You can't go there, it looks like it's protected by an energy barrier! Listen to the sentence with \"Ctrl + 1\" then type it correctly to switch it off.", "" + input_text, WHITE_HEIGHT)

    while shield_challenge_conditions[spot]:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                        
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    cleaned_input = clean_input(input_text)
                    words_user = cleaned_input.split()
                    wrong_words = []
                    correct_words = []

                    if challenge == "search":
                        if cleaned_input == phrase or cleaned_input == cheat:
                            if cleaned_input == phrase:
                                sound['search_success_'].play()
                            
                            elif cleaned_input == cheat:
                                sound['search_success_'].play()  # same sound as a success...
                                sound['cheat_ff_'].play()  # ...plus "full flemme" (cheat code)

                            display_nal(nextimage, "Once decoded, you get the following code: \"the code is the code\", clever, huh... At the front door, type exactly everything between the quotation marks. You can take a moment to write it down, or come back to read it again.", "", WHITE_HEIGHT)
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
                            sound['failed_chall_'].play()
                            display_w_text = True
                            input_text = ''

                    elif challenge == "trap" or challenge == "shield":
                        if cleaned_input == phrase:
                            sound['shield_success_'].play()
                            shield_challenge_conditions[spot] = False
                            return True  # Successfully wrote the phrase
                        
                        elif cleaned_input == cheat:
                            sound['shield_success_'].play()  # same sound as a success...
                            sound['cheat_ff_'].play()  # ...plus "full flemme" (cheat code)
                            shield_challenge_conditions[spot] = False
                            return True  # Cheated
                                        
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

                elif event.key == K_LCTRL or event.key == K_RCTRL:
                    ctrl_pressed = True
                
                elif ctrl_pressed and event.key == k:
                    speak(phraseg, 'en')
                    ctrl_pressed = False
                
                elif event.key == pygame.K_BACKQUOTE or event.key == pygame.K_CARET:  
                    input_text = input_text

                elif event.key == K_ESCAPE and escape:
                    sound['shield_esc_'].play()
                    input_text = ""
                    return False  # Player wants to exit this challenge without advancing to the next spot

                else:
                    input_text += event.unicode

                if display_w_text:
                    wrong_words_str = ', '.join(wrong_words)
                    correct_words_str = ', '.join(correct_words)
                    display_nal(nextimage, "That's not quite it, but you're almost there. *** Wrong word(s): " + wrong_words_str + "; Correction: " + correct_words_str + " ***", "" + input_text, WHITE_HEIGHT)
                
                else:
                    display_nal(nextimage, "You can't go there, it looks like it's protected by an energy barrier! Listen to the sentence with \"Ctrl + 1\" then type it correctly to switch it off.", "" + input_text, WHITE_HEIGHT)

                pygame.display.flip()
            
            elif event.type == KEYUP and event.key in (K_LCTRL, K_RCTRL):
                    ctrl_pressed = False

    return False  # Challenge failed, keep player at the same spot
