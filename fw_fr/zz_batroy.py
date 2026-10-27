from z_lvl1 import lvl1
from z_lvl2 import lvl2
from z_lvl3 import lvl3
from z_lvlu import lvlu
import sys
import pygame
from pygame.locals import *
from modules3.draw_wrap_clean import draw_text, wrap_text

# Initialize Pygame
pygame.init()

# Game title (window caption)
GAME_TITLE = "Bataille Royale du Français"

# Dimensions of the window
WIDTH, HEIGHT = 1060, 700
WHITE_HEIGHT = 125  # The height of the white band at the bottom for user input

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_TITLE)

from modulesu.data_import import list_quests

# Load the menu background image
menu = pygame.image.load('files/background/menu.jpg')

# Level 4 quests, listed under the level 4 button: '4a' = first quest, '4b' = second one...
# (a new files/data/dataNN.py quest shows up here by itself)
QUESTS = list_quests('files/data')
QUEST_FILES = {f'4{letter}': file_name for letter, file_name, title in QUESTS}


def draw_quest_panel(surface):
    if not QUESTS:
        return
    # under the level 4 button of menu.jpg (button: x 742-998, y 204-374, same top as level 1);
    # with 4 quests the panel ends level with the bottom of the level 3 button (y 493)
    x, y, w = 695, 386, 350
    font_title = pygame.font.Font(None, 26)
    size = 24 if len(QUESTS) <= 5 else 20
    font = pygame.font.Font(None, size)
    lines = []
    for letter, file_name, title in QUESTS:
        text = f'4{letter}  {title}'
        while font.size(text)[0] > w - 24 and len(text) > 8:
            text = text[:-2].rstrip() + '…'
        lines.append(text)
    line_h = font.get_linesize() + 1  # +1: room for capital accents (É)
    h = 10 + font_title.get_linesize() + len(lines) * line_h + 4
    y = min(y, 596 - h)
    box = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.rect(box, (255, 255, 255, 228), box.get_rect(), border_radius=16)
    pygame.draw.rect(box, (0, 0, 0, 255), box.get_rect(), width=2, border_radius=16)
    surface.blit(box, (x, y))
    surface.blit(font_title.render("Choisir une quête :", True, (170, 20, 20)), (x + 12, y + 7))
    ty = y + 8 + font_title.get_linesize()
    for line in lines:
        rendered = font.render(line, True, (0, 0, 0))
        # a capital accent (É) makes the rendered line taller at the top: keep the baseline in place
        surface.blit(rendered, (x + 12, ty - max(0, rendered.get_height() - font.get_height())))
        ty += line_h


draw_quest_panel(menu)
screen.blit(menu, (0, 0))
pygame.display.flip()


def reset_window():
    """Levels can change the window size (level 1 is smaller): restore the menu window."""
    global screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    display_nal(menu, text_menu, "", WHITE_HEIGHT)


# Function to display text and images
def display_nal(image, info_text, player_text, wrectangle):
    screen.blit(image, (0, 0))

    font = pygame.font.Font(None, 26)

    # Wrap info text
    info_lines = wrap_text(info_text, font, WIDTH - 20)
    for i, line in enumerate(info_lines):
        draw_text(screen, line, (10, HEIGHT - wrectangle + 34 + i * font.get_linesize()), font)

    # Wrap player's text
    player_lines = wrap_text(player_text, font, WIDTH - 20)
    player_start_pos = HEIGHT - wrectangle + (len(info_lines) * font.get_linesize()) + 40
    for i, line in enumerate(player_lines):
        draw_text(screen, line, (10, player_start_pos + i * font.get_linesize()), font)

    pygame.display.flip()

# Text for the menu
text_menu = "Bonjour et bienvenue dans la Bataille Royale du Français, où vous perfectionnerez votre écriture tout en vous amusant (enfin, j'espère). Tapez le numéro du niveau puis Entrée : 1, 2, 3, ou 4 pour une quête surprise (4a, 4b... pour choisir une quête de la liste). 'go' reprend un niveau 4 interrompu, 'credits' pour les crédits, 'exit' pour quitter."
text_credits = "CRÉDITS : projet de fan gratuit et non commercial, fait à la maison pour aider les enfants à apprendre à écrire. Sans lien avec Epic Games (Fortnite), Google, Nintendo, Pokémon, Roblox, Marvel, DC, Lucasfilm ou qui que ce soit d'autre. Les personnages, images, sons et marques appartiennent à leurs propriétaires. Voix : Google Text-to-Speech. Appuyez sur une touche pour revenir."
textn_menu = "Cette réponse ne correspond pas aux choix proposés : tapez le numéro du niveau (1, 2, 3, 4, ou 4a, 4b... pour une quête choisie) puis Entrée, ou 'exit' pour quitter."

# Main loop
level = True
one = True
decoy = 'taehc'  # cheat code (all levels)
edoc2 = 'code'    # door code of level 2 (the card says the code is... 'code')
edoc3 = 'turbo'   # car-key code of level 3

while level:
    input_text = ''
    display_w_text = False
    show_credits = False

    # Initial instructions display
    display_nal(menu, text_menu, "", WHITE_HEIGHT)

    while one:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    choice = input_text.strip().lower()
                    input_text = ''
                    display_w_text = False

                    if choice in ("exit", "quitter"):
                        level = False
                        one = False
                        break

                    elif choice == "1":
                        lvl1(decoy, edoc2)
                        reset_window()

                    elif choice == "2":
                        lvl2(decoy, edoc2)
                        reset_window()

                    elif choice == "3":
                        lvl3(decoy, edoc3)
                        reset_window()

                    # Level 4 = Ultimate Mission (old level 'u'; 'u' still works)
                    elif choice in ("4", "u"):
                        lvlu()
                        reset_window()

                    # Level 4 with a chosen quest: '4a', '4b'... (list on the menu picture)
                    elif choice in QUEST_FILES:
                        lvlu('', QUEST_FILES[choice])
                        reset_window()

                    elif choice in ("credits", "crédits"):
                        show_credits = True

                    elif choice == "go":
                        lvlu('y')
                        reset_window()

                    else:
                        display_w_text = True

                elif event.key == K_BACKSPACE:
                    input_text = input_text[:-1]

                else:
                    input_text += event.unicode

                if show_credits and input_text == '':
                    display_nal(menu, text_credits, input_text, WHITE_HEIGHT)
                    show_credits = False
                elif display_w_text:
                    display_nal(menu, textn_menu, input_text, WHITE_HEIGHT)
                else:
                    display_nal(menu, text_menu, input_text, WHITE_HEIGHT)

                pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
