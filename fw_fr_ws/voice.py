import sys

# Voice of the game.
# - On the computer (python main.py): Google Text-to-Speech (gTTS), needs internet.
# - In a web browser (pygbag): the browser's own speech engine (Web Speech API), no Google call.
WEB = sys.platform == 'emscripten'

if WEB:
    import platform

    _JS = r"""
window.brfSpeak = function (text, lang) {
  try {
    var s = window.speechSynthesis;
    if (!s) { return false; }
    s.cancel();
    var u = new SpeechSynthesisUtterance(text);
    var want = (lang === 'fr') ? ['fr-CA', 'fr'] : ['en-CA', 'en-US', 'en'];
    u.lang = want[0];
    var voices = s.getVoices() || [];
    for (var i = 0; i < want.length && !u.voice; i++) {
      for (var j = 0; j < voices.length; j++) {
        var vl = (voices[j].lang || '').replace('_', '-');
        if (vl === want[i] || (want[i].length === 2 && vl.slice(0, 2) === want[i])) { u.voice = voices[j]; break; }
      }
    }
    u.rate = 0.9;
    s.speak(u);
    window.brfSpoken = (window.brfSpoken || 0) + 1;
    return true;
  } catch (e) { console.log('voice error', e); return false; }
};
if (window.speechSynthesis) { window.speechSynthesis.getVoices(); }
"""
    _ready = False

    def speak(text, lang='fr', retries=2, delay=1):
        """Read the text out loud with the browser's voice (doesn't wait for the end)."""
        global _ready
        try:
            if not _ready:
                platform.window.eval(_JS)
                _ready = True
            platform.window.brfSpeak(text, lang)
            return True
        except Exception as e:
            print(f"Voice unavailable in this browser: {e}")
            return False

else:
    import pygame
    import io
    import time

    def speak(text, lang='fr', retries=2, delay=1):
        """Read the text out loud with Google Text-to-Speech (needs internet).
        If there is no internet (or Google refuses), the game keeps going without the voice
        instead of crashing."""
        for attempt in range(retries):
            try:
                from gtts import gTTS as gtts  # type: ignore  (pip install gtts)
                tts = gtts(text=text, lang=lang)
                mp3_fp = io.BytesIO()
                tts.write_to_fp(mp3_fp)
                mp3_fp.seek(0)
                pygame.mixer.init()
                pygame.mixer.music.load(mp3_fp, 'mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                return True
            except Exception as e:  # no internet, Google error, audio error...
                print(f"Voice attempt {attempt + 1} failed: {e}")
                if attempt < retries - 1:
                    time.sleep(delay)
        print("Voix indisponible (vérifiez la connexion internet). Le jeu continue sans la voix.")
        return False
