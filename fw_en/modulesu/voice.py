from gtts import gTTS as gtts  # type: ignore
import pygame
import io
import time


def speak(text, lang='en', retries=2, delay=1):
    """Read the text out loud with Google Text-to-Speech (needs internet).
    If there is no internet (or Google refuses), the game keeps going without the voice
    instead of crashing."""
    for attempt in range(retries):
        try:
            tts = gtts(text=text, lang=lang)

            # Use an in-memory bytes buffer
            mp3_fp = io.BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)  # Rewind the buffer to the beginning

            # Initialize pygame mixer
            pygame.mixer.init()

            # Load the sound from the in-memory bytes buffer
            pygame.mixer.music.load(mp3_fp, 'mp3')
            pygame.mixer.music.play()

            # Wait until the speech is done playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            return True  # Success
        except Exception as e:  # no internet, Google error, audio error...
            print(f"Voice attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)  # Wait before retrying
    print("Voice unavailable (check the internet connection). The game continues without it.")
    return False
