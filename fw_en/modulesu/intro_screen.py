# Start screen of levels 2, 3 and 4: the top of a picture + a white zone with the instructions.
# The white zone grows with the amount of text (the picture is cropped), so each level can say
# what it needs. Words between single quotes ('look', 'info'...) are written in blue: they are
# the words to type. Lines starting with "- " are bullet points.
import re
import sys
import pygame
from pygame.locals import QUIT, KEYDOWN

TEXT = (20, 20, 20)
KEYWORD = (20, 70, 190)
TITLE = (170, 20, 20)


def _segments(line):
    """Split a line into (text, is_keyword) pieces; keywords are the parts between single quotes
    that contain no space-only content, e.g. 'look' or 'e. attack'."""
    pieces = []
    pos = 0
    for m in re.finditer(r"(?<![^\s(])'[^'\s][^'\n]{0,40}'(?=[\s,.;:)!?]|$)", line):
        if m.start() > pos:
            pieces.append((line[pos:m.start()], False))
        pieces.append((m.group(0), True))
        pos = m.end()
    if pos < len(line):
        pieces.append((line[pos:], False))
    return pieces


def _layout(lines, font, font_bold, max_width, indent):
    """Word-wrap the lines. Returns a list of rows: (x_offset, [(word, is_keyword, space_before), ...], bullet_start)."""
    rows = []
    for line in lines:
        bullet = line.startswith('- ')
        if bullet:
            line = line[2:]
        x0 = indent if bullet else 0
        words = []
        glue = False  # True when the previous piece did not end with a space
        for text, kw in _segments(line):
            if kw:
                words.append((text, True, not glue))
                glue = True
            else:
                parts = text.split(' ')
                for i, w in enumerate(parts):
                    if w:
                        words.append((w, False, not (i == 0 and glue)))
                glue = not text.endswith(' ')
        space = font.size(' ')[0]
        row, width, first = [], 0, True
        for w, kw, sp in words:
            f = font_bold if kw else font
            ww = f.size(w)[0] + (space if sp and row else 0)
            if row and sp and x0 + width + ww > max_width:
                rows.append((x0, row, bullet and first))
                first = False
                row, width = [], 0
                ww = f.size(w)[0]
            row.append((w, kw, sp))
            width += ww
        rows.append((x0, row, bullet and first))
    return rows


def show_intro(screen, image, title, lines, footer, width=1060, height=700, focus=0.42, min_picture=150):
    """Show the start screen and wait for a key. It is redrawn regularly, so it never stays hidden
    behind the loading picture (Windows sometimes keeps showing an old picture after a long loading)."""
    font = pygame.font.Font(None, 25)
    font_bold = pygame.font.Font(None, 25)
    font_bold.set_bold(True)
    font_title = pygame.font.Font(None, 36)
    font_title.set_bold(True)
    indent = 22
    rows = _layout(lines, font, font_bold, width - 40 - indent, indent)
    line_h = font.get_linesize() + 2
    text_h = 16 + font_title.get_linesize() + 8 + len(rows) * line_h + 10 + font_bold.get_linesize() + 14
    picture_h = max(min_picture, height - text_h)

    # top of the picture, centred on 'focus' (0 = top, 1 = bottom of the picture part)
    img_h = min(image.get_height(), 600)
    top = int(max(0, min(img_h - picture_h, focus * img_h - picture_h / 2)))

    def draw():
        screen.fill((255, 255, 255))
        screen.blit(image, (0, 0), pygame.Rect(0, top, width, picture_h))
        pygame.draw.line(screen, (200, 200, 200), (0, picture_h), (width, picture_h), 2)
        y = picture_h + 14
        screen.blit(font_title.render(title, True, TITLE), (20, y))
        y += font_title.get_linesize() + 8
        for x0, row, bullet_start in rows:
            x = 20 + x0
            if bullet_start:
                pygame.draw.circle(screen, TITLE, (20 + indent // 2 - 2, y + line_h // 2 - 2), 4)
            for j, (w, kw, sp) in enumerate(row):
                f = font_bold if kw else font
                if sp and j > 0:
                    x += font.size(' ')[0]
                surf = f.render(w, True, KEYWORD if kw else TEXT)
                screen.blit(surf, (x, y))
                x += f.size(w)[0]
            y += line_h
        y += 6
        foot = font_bold.render(footer, True, TITLE)
        screen.blit(foot, (width - 20 - foot.get_width(), y))
        pygame.display.flip()

    pygame.event.clear()  # keys pressed during the loading don't skip this screen
    draw()
    clock = pygame.time.Clock()
    elapsed = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                return
            else:  # window shown again, focus, resize...: redraw
                draw()
        elapsed += clock.tick(30)
        if elapsed > 700:
            draw()
            elapsed = 0
