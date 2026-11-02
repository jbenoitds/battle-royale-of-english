# Web version, step 3 of build_web.sh: turn zz_batroy.py (menu) into main.py with an async main loop.
import sys, re
p = sys.argv[1]
s = open(p + '/zz_batroy.py', encoding='utf-8').read()
def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old, s.count(old))
    s = s.replace(old, new)
rep("import sys\nimport pygame\n", "import sys\nimport asyncio\nimport pygame\n")
rep("""from modules3.draw_wrap_clean import draw_text, wrap_text
""", """from modules3.draw_wrap_clean import draw_text, wrap_text

WEB = sys.platform == 'emscripten'  # True when the game runs in a web browser (pygbag)
if WEB:
    import websave  # web: the level 4 save ('go') and the played quests are kept in the browser
""")
rep("Voice: Google Text-to-Speech.", "Voice: \" + (\"your browser's speech synthesis\" if WEB else \"Google Text-to-Speech\") + \".")
# main loop -> async main()
head, loop = s.split("# Main loop\n")
loop = loop.replace("# Quit Pygame\npygame.quit()\nsys.exit()\n", "")
consts, rest = loop.split("while level:", 1)
body = "while level:" + rest
for name in ("lvl1(", "lvl2(", "lvl3(", "lvlu("):
    body = body.replace(" " + name, " await " + name)
body = body.replace("""                    if choice in ("exit", "quit"):
                        level = False""", """                    if choice in ("exit", "quit") and WEB:
                        # in a browser the game can't close its own tab
                        display_nal(menu, "To quit, just close the browser tab. (Or type a level to keep playing.)", "", WHITE_HEIGHT)
                        continue

                    if choice in ("exit", "quit"):
                        level = False""")
body = body.replace("""    while one:
        for event in pygame.event.get():""", """    while one:
        await asyncio.sleep(0)  # web: let the browser draw (one frame)
        for event in pygame.event.get():""", 1)
assert "WEB:" in body and "await asyncio.sleep(0)" in body
body = "\n".join(("    " + l if l.strip() else l) for l in body.split("\n"))
s = head + "# Main loop\n" + consts.replace("level = True\none = True\n", "") + \
    "\nasync def main():\n    level = True\n    one = True\n" + body.rstrip() + \
    "\n\n    pygame.quit()\n    if not WEB:\n        sys.exit()\n\n\nasyncio.run(main())\n"
open(p + '/main.py', 'w', encoding='utf-8').write(s)
open(p + '/zz_batroy.py', 'w', encoding='utf-8').write(
    "# The game now starts from main.py (needed for the web version).\n"
    "# This file is kept so 'python zz_batroy.py' still works.\n"
    "import runpy\nrunpy.run_path('main.py', run_name='__main__')\n")
