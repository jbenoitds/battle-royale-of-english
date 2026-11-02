WEB VERSION OF "BATAILLE ROYALE DU FRANÇAIS" (work in progress)
===============================================================

This folder does NOT hold a copy of the game. It holds the tools that turn the
normal French game (folder fw_fr) into a version that plays in a web browser.
So when you change the French game, rebuilding the web version picks up your changes.

How the web version works
- pygbag (https://github.com/pygame-web/pygbag) runs Python + pygame inside the browser.
- build_web.sh copies fw_fr, then changes the copy (fw_fr itself is never touched):
  1. leaves out the dev scripts, old drafts (files/data/arch) and saves;
  2. sounds MP3 -> OGG (browsers play OGG reliably; also 3x smaller);
  3. code: the game loops become "async" (asyncify.py: a browser tab freezes if a loop
     never hands control back), the menu becomes main.py (make_main.py), the voice uses the
     browser's speech engine instead of Google (voice.py), 'exit' explains to close the tab;
  4. pygbag builds the site with the page template brf_fr.tmpl (French loading texts,
     accent dead keys fixed, Ctrl+1..9 / Ctrl+Q kept away from the browser).
- Desktop: the transformed copy still runs with  python main.py  (voice = gTTS as before).

Files
  build_web.sh       the build (run in the cloud workspace or any Linux/Mac/WSL shell)
  asyncify.py        step 3: async game loops
  make_main.py       step 3: zz_batroy.py -> main.py
  voice.py           browser voice (Web Speech API) / gTTS on the computer
  web_images.py      step 2b: big PNG -> JPG (code updated), lazy loading of backgrounds
  weblazy.py         copied into the game: backgrounds loaded when shown (last 40 kept)
  websave.py         copied into the game: files/saves/ kept in the browser storage
  make_template.py   makes brf_fr.tmpl from pygbag's default.tmpl (fr or en)
  brf_fr.tmpl        the page template used by the build
  favicon.png        browser tab icon

Status: see PROGRESS at the end.

PROGRESS
--------
Chunk 1 (2026-10-27) DONE: menu + level 1 play in the browser (tested in headless Chromium):
  menu, credits, level 1 to the end and back to the menu, Ctrl+1 voice, typed é, dead-key ê
  (no stray "["), 'exit' message. Proof-of-concept build = menu + level 1 only, 10 MB.
Chunk 2 (2026-10-27) DONE: the whole game builds for the browser: 60 MB download (was
  186 MB): 155 PNG -> JPG, sounds OGG; backgrounds of levels 2/3/4 load when shown; level 4
  save and played quests survive closing the tab (localStorage, key prefix
  'bataille_royale_fr:'). Tested in headless Chromium: level 2 (move, cheat end), level 3
  (move, cheat end), level 4 quest 4a (start page, arrows, 'ville' map, 'quitter', page
  reload, 'go' resumes). Same tests on desktop with the transformed copy.
  Kept Ctrl+1..4 for the voice (the page asks the browser not to switch tabs): to check
  on a real PC browser; fallback = other keys.
Chunk 3 TODO: hosting (GitHub Pages or itch.io) + test on a real PC browser
  (voice quality, real keyboard: Ctrl+1 must not switch tabs, accents).
Known: the menu/level texts drawn with pygame's default font have slightly uneven letter
  spacing in the browser (readable).
