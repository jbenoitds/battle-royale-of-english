# Load a sound file (used by every sound loader of the game).
#
# Most sounds are loaded normally. Only the files with a BIG ID3 tag at the start are fixed:
# the English copy of the sounds got a large "content credentials" ID3 tag when they were copied
# to Google Drive (the audio itself is identical to the French files), and pygame on Windows
# plays some of those files badly (the bus sound of level 1 stayed silent).
# For those files the big tag is replaced by a tiny empty one. The tiny tag must stay: without
# any ID3 tag, pygame on Windows doesn't recognise some MP3 files (the "MPEG-2" ones, like the
# level 1 bus sound) and they play silently.
# Any problem: normal loading.
import io
import pygame

BIG_TAG = 1024  # bytes; normal tags are much smaller
TINY_TAG = b'ID3\x03\x00\x00' + bytes([0, 0, 0, 16]) + bytes(16)  # empty ID3v2.3 tag, 16 bytes of padding


def load_sound(path):
    try:
        with open(path, 'rb') as f:
            data = f.read()
        if data[:3] == b'ID3' and len(data) > 10:
            size = (data[6] << 21) | (data[7] << 14) | (data[8] << 7) | data[9]
            if data[5] & 0x10:  # tag footer
                size += 10
            audio = data[10 + size:]
            if size > BIG_TAG and audio[:1] == b'\xff':  # audio starts right after the tag
                return pygame.mixer.Sound(file=io.BytesIO(TINY_TAG + audio))
    except Exception:
        pass
    return pygame.mixer.Sound(path)
