# fw_en: English version changes (2026-09-24)

These 59 files replace the ones with the same paths in a copy of `fw` (= `fw_en`). The French `fw` is untouched.

## Done
- **UI text:** menu, missions 1/2/3/h/u, battle, trap, shield, search, TV and animal messages, plus the credits screens are now English. The window title is "Battle Royale of English".
- **Typed commands:** `fouiller` → `search`, `avant/gauche/droite/arrière` → `forward/left/right/back`, `attaque` → `attack`, `ennemi` → `enemy`, `chef` → `boss`, `titre` → `title`, `énigme1-5` → `riddle1-5`. The `full flemme` cheat is now `so lazy`. `go`, `go back`, `off` and `exit` are unchanged.
- **Voice:** gTTS speaks English (`lang='en'`).
- **Answer checking:** phrases are lowercased when loaded, and curly apostrophes (’) typed by the player count as straight ones ('). This means "I" can be written normally in the text files.
- **Dictation lists** (`files/texts/phrases_pet/moy/gde.txt`): 48 new English sentences each, for grades 2–4. They keep the same themes and silly humour as the French lists ("the feet stink").
- **Verb lists** (`files/texts/conjugaisons_*.txt`): 18 lines each, using be/have/go/do/want/come in the present, past and future. pet = I/you, moy = I/you/he-she/we, gde = I/you/he-she/we/they.
- **Level u data** (`files/data/data10.py`): translated. The level code is now `jewels` (6 letters). The two "words of the week" phrases in `z_lvlu.py` are now English.
- **Anonymization (code/data):** the child's full name, the town name, the friends' names (now `friend1-3`) and real store names (now `grocery`, `hardware`, `office`, `pawnshop`, `corner_store`, `dollar_store`) are gone. The chatbot prompt now asks for English.
- Removed: the duplicate files `modules3/special_*-jbenoitds.py` (they were identical copies).

## Still to do
- **Images:** crop the Street View UI and addresses (220 images in missionu), cover the names in the level-h photos, and strip EXIF. Check the loader and menu images for text baked into the picture.
- `files/data/arch/*.py` (old quest data) is still French and may contain the same personal names. Delete it from fw_en or anonymize it.
- `files/texts/phrases_ce2.txt` (unused) is still French.
- Some item names typed by the player are odd in English (`guitare`, `hiking_bag`). They are also image keys, so rename both together if needed.
- Credits/disclaimer screen (fan project, non-commercial).
- Test run: `python zz_batroy.py` from inside fw_en (every file compiles; not played yet).
