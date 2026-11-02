import pygame
import sys
from pygame.locals import *
from modules1.display import display_nal
from modules1.soundfix import load_sound
from modules3.voice import speak

def lvl1(decoy, edoc):

    def clean_input(user_input):
        return user_input.replace('\u2019', "'").strip().lower()

    def batroy(screen, nextimage, texty, textn, phrase, k, son):
        input_text = ''
        ctrl_pressed = False
        wrong_words = []
        correct_words = []
        display_w_text = False
        word_err = False
        flags = False
        flagi = ''
        if decoy == edoc:
            print('saperlipopette')

        display_nal(screen, texty, "", WHITE_RECT_HEIGHT, nextimage)
        one = True
        while one:
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

                        if cleaned_input in [phrase, decoy]:  # decoy = cheat code (taehc)
                            input_text = ''
                            son.play()
                            if cleaned_input == decoy and cleaned_input != phrase:
                                snd_cheat.play()  # "full flemme", on top of the normal sound
                            one = False

                        else:
                            for user_word, correct_word in zip(words_user, phrase.split()):
                                if user_word != correct_word:
                                    wrong_words.append(user_word)
                                    correct_words.append(correct_word)
                            snd_fail.play()  # wrong sentence
                            display_w_text = True
                            input_text = ''
            
                    elif event.key == K_BACKSPACE:
                        input_text = input_text[:-1]
                        word_err = False  # correcting: the warning goes away until the next space

                    elif event.key == K_LCTRL or event.key == K_RCTRL:
                        ctrl_pressed = True
                        
                    elif ctrl_pressed and event.key == k:
                        speak(f'"{phrase}"', 'en')
                        ctrl_pressed = False

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
                        display_nal(screen, textn + " *** Wrong word(s): " + wrong_words_str + "; Correction: " + correct_words_str + " ***", "" + input_text, WHITE_RECT_HEIGHT, nextimage)
                       
                        if word_err:
                            display_nal(screen, f"!!! WATCH OUT !!! Wrong word: \"{flagi}\"._____ Read it again: does it look right? Tips: their / there / they're; to / too / two; its / it's? Verb: past tense with -ed, or irregular (ran, ate, went)? Plural: -s or -es? Silent letters (knee, write, lamb)? Double letters (happy, running)?", "" + input_text, WHITE_RECT_HEIGHT, nextimage)                    
                            if flags:
                                snd_bip.play()  # bip-bip: wrong word (once per word)
                                flags = False

                    elif word_err:
                        display_nal(screen, f"!!! WATCH OUT !!! Wrong word: \"{flagi}\"._____ Read it again: does it look right? Tips: their / there / they're; to / too / two; its / it's? Verb: past tense with -ed, or irregular (ran, ate, went)? Plural: -s or -es? Silent letters (knee, write, lamb)? Double letters (happy, running)?", "" + input_text, WHITE_RECT_HEIGHT, nextimage)                    
                        if flags:
                            snd_bip.play()  # bip-bip: wrong word (once per word)
                            flags = False

                    else:
                        display_nal(screen, texty, "" + input_text, WHITE_RECT_HEIGHT, nextimage)

                    pygame.display.flip()
        
                elif event.type == KEYUP and ctrl_pressed and event.key == K_q:
                    one = False
                    return

                elif event.type == KEYUP:
                    if event.key == K_LCTRL or event.key == K_RCTRL:
                        ctrl_pressed = False
            

    # Dimensions of the window
    WHITE_RECT_HEIGHT = 133
    WIDTH, HEIGHT = 1025, 700  # was 667: the typed text was half hidden at the bottom
    INSTRU_HEIGHT = 165
    FONT_SIZE = 26
    TEXT_COLOR = (0, 0, 0)

    # Load images
    images = [
        pygame.image.load(f'files/background/mission1/{i}p.jpg') for i in range(1, 6)
    ]
    lobby_ava = pygame.image.load('files/background/mission1/lobby_ava.jpg')

    # Load sounds
    sounds = load_sound('files/sound/mission1/s.mp3')
    snd_bus = load_sound('files/sound/mission1/bus_debut_.mp3')  # bus sound, played on the first picture
    soundsf = load_sound('files/sound/mission1/sf.mp3')
    # same error / cheat sounds as the other levels
    snd_bip = load_sound('files/sound/mission2/blipblip.mp3')         # wrong word (checked at each space)
    snd_fail = load_sound('files/sound/mission2/failed_chall_.mp3')   # wrong sentence (Enter)
    snd_cheat = load_sound('files/sound/mission2/cheat_ff_.mp3')      # cheat code: "full flemme"

    # Ensure Pygame is initialized
    if not pygame.get_init():
        pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Battle Royale of English")
    nextimage = lobby_ava

    phrase1 = "i jump off the bus"
    phrase2 = "you dive down fast"
    phrase3 = "we open our glider"
    phrase4 = "she lands on the house"

    snd_bus.play()  # the bus, as soon as the first picture of the level shows
    batroy(screen, images[0], "Mission 1a: Your mission, should you choose to accept it, is to get to know this game... and to check that it works. Unlock an action by typing its instruction, then press Enter. To hear the instruction, press 'Ctrl + 1'.", "Mission 1a: That last sentence wasn't quite right. Try again, I know you can do it. To hear the instruction again, press 'Ctrl + 1';", phrase1, K_1, sounds)
    batroy(screen, images[1], "Mission 1b: Well done! You typed the instruction correctly and unlocked the Jump off the bus action! For the next one, press 'Ctrl + 2' to hear its instruction and type it. Here, Ctrl + 1 shouldn't work, in theory...", "Mission 1b: That last sentence wasn't quite right. Try again, I know you can do it. To hear the instruction again, press 'Ctrl + 2';", phrase2, K_2, sounds)
    batroy(screen, images[2], "Mission 1c: Excellent! New action unlocked! Well, same thing here, but with a new instruction. Press Ctrl + 3 to... you know what!", "Mission 1c: That last sentence wasn't quite right. Try again, I know you can do it. To hear the instruction again, press 'Ctrl + 3';", phrase3, K_3, sounds)
    batroy(screen, images[3], "Mission 1d: Woohoo! You're on fire! Another action unlocked. Last step and last action, with... you guessed it, Ctrl + 4. If you like this game so far... well, you can't rate it, but hey, it's nice to hear!", "Mission 1d: That last sentence wasn't quite right. Try again, I know you can do it. To hear the instruction again, press 'Ctrl + 4';", phrase4, K_4, soundsf)

    display_nal(screen, "Mission 1 Complete. Congratu-bravo-lations !!! You have finished the first mission of the 'Battle Royale of English'.", "", WHITE_RECT_HEIGHT, images[4])

    while True:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                return
