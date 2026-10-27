BATTLE ROYALE OF ENGLISH
========================

A small home-made game for practising English spelling and writing while having
fun. You listen to a sentence, type it without mistakes, and move forward in the
adventure: traps, energy shields, battles against characters and a final mission
in a neighbourhood.

Free, non-commercial fan project. Not affiliated with Epic Games (Fortnite),
Google, Nintendo, Pokemon, Roblox, Marvel, DC, Lucasfilm or anyone else. All
characters, images, sounds and trademarks belong to their owners.
(In the menu, type 'credits' to see this notice in the game.)


1. WHAT YOU NEED
----------------
- A computer with Python 3 (version 3.10 or newer): https://www.python.org
- Two Python modules, installed once. In a terminal (Command Prompt on Windows),
  type:
      pip install pygame gtts
- Internet, for the voice that reads the sentences (Google Text-to-Speech).
  Without internet the game still works, just without the voice.
- Speakers or headphones.


2. STARTING THE GAME
--------------------
The game has to be started from its own folder (the one with this file):
      cd "path/to/fw_en"
      python zz_batroy.py

Windows tip: in File Explorer, open the game folder, type cmd in the address
bar, press Enter, then type: python zz_batroy.py


3. THE MENU
-----------
Type your choice, then press Enter:
  1        Level 1 - Intro & Commands
  2        Level 2 - Moving & Events
  3        Level 3 - Battles & Objectives
  4        Level 4 - Ultimate Mission (in a neighbourhood), surprise quest
  4a, 4b.. Level 4 with the quest of your choice (the list of quests is shown
           on the menu picture, under the level 4 button)
  go       pick the Ultimate Mission back up where you left it
  credits  credits and notice
  exit     quit the game


4. HOW TO PLAY
--------------
Everywhere in the game: type on the keyboard, then press Enter.
Capital letters don't matter, but spelling does: it's a writing game!

Hear a sentence: hold Ctrl and press 1 (Ctrl + 1).
When there are several sentences, it's Ctrl + 2, Ctrl + 3, etc.
Bip-bip! = the word you just typed is wrong: each time you press the space bar,
the game checks the last word. Fix it (Backspace) before going on.
Mip-mip! (battles) = you forgot the weapon number (1., 2. or 3.) at the start.

Levels 2, 3 and 4 start with a page that explains the controls of the level.
Press any key to start. In the game, type 'info' then Enter to see them again.

LEVEL 1 - Intro & Commands
  Listen to the sentence (Ctrl + 1, then Ctrl + 2, 3 and 4) and type it without
  mistakes to unlock each action.

LEVEL 2 - Moving & Events
  You're locked inside the Lavish Lair. Find the card with the door code written
  on it, then go back to the entrance and type the code to get out.
    forward / left / right / back   move around
    look         search where you are (the card only shows up once all the
                 traps and shields are disabled)
    info         show the controls on the screen ('info' again: the goal)
    mission      see the goal again
    quit         go back to the menu
  Trap: type the sentence you hear to get free.
  Energy shield: type the sentence to get through (Esc to step back).

LEVEL 3 - Battles & Objectives
  On your way out of the Lavish Lair: find the car keys (in the library) and an
  ice-cold Nuka-Cola (in the kitchen), then type the key code at the entrance
  (the starting point).
    same commands as level 2 (forward, left, right, back, look, info,
    mission, quit)
  Battles: listen to a sentence with Ctrl + 1, 2 or 3, then type the weapon
  number followed by the sentence, for example:   1. the cat is asleep
    1.  pistol       (short sentence,  -1 life, 2 bullets)
    2.  machine gun  (medium sentence, -2 lives)
    3.  shotgun      (long sentence,   -3 lives, 1 shell)

LEVEL 4 - Ultimate Mission
  A quest in a neighbourhood, different every time (4 quests, picked at
  random without repeats; or choose one in the menu with 4a, 4b, 4c, 4d):
  find one or two objects thanks to the clues, beat three enemies, then the
  chief (watch out for traps and shields).
    Arrow keys   up = forward, left / right = turn, down = turn around
    or W A S D   (W = forward, A / D = turn, S = turn around; you move as
                 soon as you press them)
    look       search for an object       title    name of the quest
    clue1      read clue 1 again          clue2    read clue 2 again
    enemy      hint about the enemies     chief    hint about the chief
    city       show / hide the map of the city (the red arrow is you; you
               can't move while it's open, Escape closes it)
    info       show / hide the controls
    quit       save and go back to the menu (then type 'go' in the menu to
               pick the game back up)
  At the right place, type 'look': three objects show up. Type the name of
  the right one (for example "bucket" or "the bucket"), then the sentence
  you hear with Ctrl + 1 to get it.
  Conjugation (Everest and the chief): Ctrl + 1, 2 or 3 tells a verb and a
  tense. Type the weapon number, then the verb conjugated with:
    1.  I and you                       1. I am you are
    2.  I, you, he/she, we              2. I am you are he is we are
    3.  I, you, he/she, we, they        (the voice says he or she)
  Everest the dog: type 'evy' and win a conjugation to charge her (3 times
  per mission), then in front of an enemy or the chief type  e. attack  to
  let her go: she gobbles them up in one bite.
  The chief comes back to life once: finish him with a conjugation.


5. IF SOMETHING DOESN'T WORK
----------------------------
- "No module named pygame" (or gtts): run  pip install pygame gtts  again.
- No voice: check the internet connection and the volume. If Google doesn't
  answer, the game keeps going without the voice.
- "No such file or directory: 'files/...'": the game wasn't started from its
  folder. First  cd  into the game folder.
- During a battle you can't leave the level: finish the battle, or close the
  window to quit the game.


6. FOR PARENTS AND TEACHERS: CHANGING THE SENTENCES
---------------------------------------------------
The sentences to listen to and type are plain text files, easy to adapt, for
example to this week's spelling list.

Where are they?  In the folder  files/texts/ :
  phrases_pet.txt         short sentences   (level 3: pistol; level 4)
  phrases_moy.txt         medium sentences  (levels 2, 3 and 4: traps,
                                             shields, searches, machine gun)
  phrases_gde.txt         long sentences    (level 3: shotgun; level 4)
  conjugaisons_pet.txt    verb tenses       (level 4: Everest and the chief)
  conjugaisons_moy.txt    verb tenses       (same)
  conjugaisons_gde.txt    verb tenses       (same)
The level 1 sentences are fixed (in z_lvl1.py).

How?
  1. Close the game.
  2. Make a copy of the file (just in case), then open it with Notepad
     (right-click > Open with > Notepad).
  3. One sentence per line. Change, add or replace lines.
  4. Save (File > Save, UTF-8 encoding, the default one).
  The game picks sentences at random every time.

Rules:
  - At least 48 lines in each phrases_*.txt and 18 in each conjugaisons_*.txt
    (level 4 uses that many). More is fine. Empty lines are ignored.
  - Write exactly what the child has to type. Capital letters don't matter,
    the game ignores them.
  - Avoid punctuation (periods, commas, exclamation marks): it would have to
    be typed too. Apostrophes (I'm, don't) are fine.
  - Verb tenses: what the voice announces, a semicolon, then what to type.
    Example:
        To be in the present (with he); I am you are he is
  - Keep the same length as the other sentences of the file (short, medium
    or long): the difficulty of the game depends on it.

The "words of the week" of level 4 (the sentences of the traps and shields)
are two lines in z_lvlu.py: open it with Notepad, search (Ctrl + F) for
"Mots de la semaine" and change the text between the quotation marks.

7. GOING FURTHER: THE LEVEL 4 QUESTS
------------------------------------
Each quest is a file  files/data/dataNN.py  (data10 to data13). To make a new
one, copy an existing quest, give it a new two-digit number (file data14.py
with 'data_id': 14) and change the texts, places and objects. The rules are
written at the top of each file.
