# Function to draw text
def draw_text(surface, text, pos, font):
    text_surface = font.render(text, True, (0, 0, 0))
    surface.blit(text_surface, pos)

# Function to wrap text
def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = ''

    for word in words:
        test_line = current_line + word + ' '
        if font.size(test_line)[0] < max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + ' '

    lines.append(current_line)
    return lines

# Function to clean user input
def clean_input(user_input):
    return user_input.replace('\u2019', "'").strip().lower()