#!/bin/sh
# Build the WEB version of the French game from the normal game folder fw_fr.
#   usage: sh build_web.sh PATH/TO/fw_fr OUT_DIR [poc]
#   needs: python 3 + pip install pygbag==0.9.3 pygame-ce ; ffmpeg
#   result: OUT_DIR/web/ (index.html + fw_fr_ws.apk/.tar.gz) = the site to upload.
# The browser page downloads Python itself from pygame-web.github.io when it opens.
set -e
TOOLS=$(cd "$(dirname "$0")" && pwd)
SRC=$1; OUT=$2; MODE=$3
mkdir -p "$OUT"; OUT=$(cd "$OUT" && pwd)
STAGE=$OUT/stage/fw_fr_ws
rm -rf "$OUT/stage"; mkdir -p "$OUT/stage"
cp -r "$SRC" "$STAGE"
cd "$STAGE"
# 1. only what the game needs (dev scripts, old drafts and saves out)
rm -rf build Autre files/data/arch files/saves/quests_played.txt
rm -f add1.py png_to_jpg.py re_charac.py recrop.py rename.py resize.py roblax.py sRGB_profile.py test.py textbox.py voicesplitter.py myrks.py zz_fortwrite.py z_data_verif_*.py checklst.md LISEZMOI.txt
find . -name __pycache__ -prune -exec rm -rf {} +
if [ "$MODE" = "poc" ]; then  # proof of concept: menu + level 1 only (small download)
  rm -rf files/background/mission2 files/background/mission3 files/background/missionu files/new_enemies files/images_enemy files/images_oth files/items files/score
fi
# 2. sounds: MP3 -> OGG (the format browsers play reliably), mono 24 kHz
find files -iname "*.mp3" -print0 | xargs -0 -P 8 -I{} sh -c 'ffmpeg -nostdin -loglevel error -y -i "$1" -vn -map_metadata -1 -ac 1 -ar 24000 -c:a libvorbis -q:a 4 "${1%.*}.ogg" && rm "$1"' _ {}
# 2b. pictures: big PNG -> JPG, backgrounds loaded when shown
cp "$TOOLS/weblazy.py" "$TOOLS/websave.py" .
python3 -I "$TOOLS/web_images.py" "$STAGE"
# 3. code: .mp3 -> .ogg, browser voice, async game loops, main.py
grep -rl --include=*.py "\.mp3" . | xargs -r sed -i 's/\.mp3/.ogg/g'
for m in modules2 modules3 modulesu; do cp "$TOOLS/voice.py" "$m/voice.py"; done
python3 -I "$TOOLS/make_main.py" "$STAGE"
python3 -I "$TOOLS/asyncify.py" "$STAGE"
# 4. web build
cd "$OUT/stage"
python3 -m pygbag --build --icon "$TOOLS/favicon.png" --template "$TOOLS/brf_fr.tmpl" --title "Bataille Royale du Français" fw_fr_ws
find fw_fr_ws -name "*-pygbag.py" -delete
rm -rf "$OUT/web"; cp -r fw_fr_ws/build/web "$OUT/web"
ls -la "$OUT/web"
