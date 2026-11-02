import pygame
import sys
from pygame.locals import *
from modules1.display import display_nal
from modules1.soundfix import load_sound
from modules3.voice import speak

def lvl1(decoy, edoc):

    def clean_input(user_input):
        return user_input.strip().lower()

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
                        speak(f'"{phrase}"', 'fr')
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
                        display_nal(screen, textn + " *** Mot(s) erroné(s): " + wrong_words_str + "; Correction: " + correct_words_str + " ***", "" + input_text, WHITE_RECT_HEIGHT, nextimage)
                       
                        if word_err:
                            display_nal(screen, f"!!! ATTENTION !!! Mot incorrect: \"{flagi}\"._____ Règles: 'à/avait'; 'mordre/mordu; 'son' (le sien)/'sont' (verbe)'? Verbe: conjugué? Accord: masculin/féminin; singulier/pluriel? Lettres muettes à la fin; sons plusieurs écritures, comme 'o'/'eau'?", "" + input_text, WHITE_RECT_HEIGHT, nextimage)                    
                            if flags:
                                snd_bip.play()  # bip-bip: wrong word (once per word)
                                flags = False

                    elif word_err:
                        display_nal(screen, f"!!! ATTENTION !!! Mot incorrect: \"{flagi}\"._____ Règles: 'à/avait'; 'mordre/mordu; 'son' (le sien)/'sont' (verbe)'? Verbe: conjugué? Accord: masculin/féminin; singulier/pluriel? Lettres muettes à la fin; sons plusieurs écritures, comme 'o'/'eau'?", "" + input_text, WHITE_RECT_HEIGHT, nextimage)                    
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
    pygame.display.set_caption("Bataille Royale du Français")
    nextimage = lobby_ava

    phrase1 = "je saute du bus"
    phrase2 = "tu plonges en piqué"
    phrase3 = "nous ouvrons notre voile"
    phrase4 = "elle se pose dans la maison"

    snd_bus.play()  # the bus, as soon as the first picture of the level shows
    batroy(screen, images[0], "Mission 1a: Votre mission, si vous décidez de l'accepter, est de vous familiariser avec ce jeu... et de vérifier s'il marche. débloquez une action en tapant son instruction, suivie de Entrée. Pour entendre l'instruction, faites 'Ctrl + 1'.", "Mission 1a: Cette dernière phrase n'était pas tout à fait correcte. Essayez encore, je sais que vous pouvez y arriver. Pour réécouter l'instruction, faites 'Ctrl + 1';", phrase1, K_1, sounds)
    batroy(screen, images[1], "Mission 1b: Bravo! Vous avez correctement tapé l'instruction et vous avez débloqué l'action Sauter du bus! Pour la suivante, faites 'Ctrl + 2' pour son instruction et tapez-là. Ici, Ctrl + 1 ne devrait pas se déclencher ici, en théorie...", "Mission 1b: Cette dernière phrase n'était pas tout à fait correcte. Essayez encore, je sais que vous pouvez y arriver. Pour réécouter l'instruction, faites 'Ctrl + 2';", phrase2, K_2, sounds)
    batroy(screen, images[2], "Mission 1c: Excellent! Nouvelle action débloquée! Bah, là c'est pareil, mais avec une nouvelle instruction. Faites Ctrl + 3 pour... vous savez quoi!", "Mission 1c: Cette dernière phrase n'était pas tout à fait correcte. Essayez encore, je sais que vous pouvez y arriver. Pour réécouter l'instruction, faites 'Ctrl + 3';", phrase3, K_3, sounds)
    batroy(screen, images[3], "Mission 1d: Wouhou! Vous êtes en feu! Encore une action de débloquée. Dernière étape et dernière action, avec... vous l'avez deviné, Ctrl + 4. Si ce jeu vous plait pour l'instant... ben vous ne pouvez pas le noter, mais bon, ça fait plaisir!", "Mission 1d: Cette dernière phrase n'était pas tout à fait correcte. Essayez encore, je sais que vous pouvez y arriver. Pour réécouter l'instruction, faites 'Ctrl + 4';", phrase4, K_4, soundsf)

    display_nal(screen, "Mission 1 Complétée. Félicibravotation !!! Vous avez terminé la première mission de la 'Bataille Royale du Français'.", "", WHITE_RECT_HEIGHT, images[4])

    while True:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                return
