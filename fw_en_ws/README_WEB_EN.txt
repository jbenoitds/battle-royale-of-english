Web version of the ENGLISH game (Battle Royale of English) - same tools as fw_fr_ws, English variants.
usage (Linux/WSL, needs python3 + pip install pygbag==0.9.3 ; ffmpeg):
    sh build_web_en.sh PATH/TO/fw_en OUT_DIR
result: OUT_DIR/web/  (index.html, favicon.png, fw_en_ws.tar.gz, fw_en_ws.apk)

English differences: brf_en.tmpl (English loading texts), voice_en.py (browser voice en-CA/en-US),
websave_en.py (browser save key 'battle_royale_en:'), make_main_en.py (English credits/exit texts).
asyncify.py, web_images.py, weblazy.py, favicon.png = same as fw_fr_ws.

Publishing:
- GitHub Pages: branch gh-pages of jbenoitds/battle-royale-of-english, folder en/ with
  index.html + favicon.png + fw_en_ws.tar.gz  (outside itch.io the page loads the .tar.gz).
  Root index.html (site_index.html here) = small page with a "Play in English" button.
  URL: https://jbenoitds.github.io/battle-royale-of-english/en/
- itch.io: zip index.html + favicon.png + fw_en_ws.apk (on itch the page loads the .apk), upload as an HTML game.
