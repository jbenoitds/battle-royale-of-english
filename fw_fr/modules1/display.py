import pygame

FONT_SIZE = 26
TEXT_COLOR = (0, 0, 0)
WIDTH, HEIGHT = 1025, 700  # same as z_lvl1.py (was 667: the typed text was cut at the bottom)

def draw_text(surface, text, pos, font):
    text_surface = font.render(text, True, TEXT_COLOR)
    surface.blit(text_surface, pos)

def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_width, _ = font.size(word + ' ')
        if current_width + word_width <= max_width:
            current_line.append(word)
            current_width += word_width
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_width = word_width

    lines.append(' '.join(current_line))
    return lines

def display_nal(screen, info_text, player_text, wrectangle, nextimage):
    screen.fill((255, 255, 255))  # the pictures are a bit shorter than the window
    screen.blit(nextimage, (0, 0))
    font = pygame.font.Font(None, FONT_SIZE)
    
    info_lines = wrap_text(info_text, font, WIDTH - 20)
    player_start_pos = HEIGHT - wrectangle + (len(info_lines) * font.get_linesize()) + 30
    # never below the bottom of the window (long messages)
    n_typed = max(1, len(wrap_text(player_text, font, WIDTH - 20)))
    player_start_pos = min(player_start_pos, HEIGHT - 6 - n_typed * font.get_linesize())

    for i, line in enumerate(info_lines):
        draw_text(screen, line, (10, HEIGHT - wrectangle + 20 + i * font.get_linesize()), font)
    
    player_lines = wrap_text(player_text, font, WIDTH - 20)
    for i, line in enumerate(player_lines):
        draw_text(screen, line, (10, player_start_pos + i * font.get_linesize()), font)

    pygame.display.flip()

def display_image_with_text(screen, image, text, pos):
    screen.blit(image, (0, 0))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, TEXT_COLOR)
    screen.blit(text_surface, pos)
    pygame.display.flip()
