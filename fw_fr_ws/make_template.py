"""Build the page template of the web version from pygbag's default template.
usage: python make_template.py default.tmpl out.tmpl fr|en"""
import sys
src, out, lang = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src, encoding='utf-8').read()
TXT = {
    'fr': ("Prêt ! Cliquez sur la page pour commencer", "Chargement, un instant…", "Téléchargement…"),
    'en': ("Ready! Click the page to start", "Loading, please wait…", "Downloading…"),
}[lang]
def rep(old, new):
    global t
    assert old in t, old
    t = t.replace(old, new)
rep('"Ready to start ! Please click/touch page"', '"%s"' % TXT[0])
rep('<div id="infobox">Loading, please wait ...</div>', '<div id="infobox">%s</div>' % TXT[1])
rep('<div class="emscripten" id="status">Downloading...</div>', '<div class="emscripten" id="status">%s</div>' % TXT[2])
rep('<html lang="en-us">', '<html lang="%s">' % lang)
KEYS = """
    <script>
    // Battle Royale keyboard fixes (registered before the game, so they run first):
    // - accent "dead keys" (^ then e = ê on French/Canadian keyboards): the browser sends a
    //   "Dead" key first; the game would type it as "[" -> hide it, only the final letter counts.
    // - Ctrl+1..9 / Ctrl+Q are game shortcuts: ask the browser not to switch tabs / quit.
    (function () {
      function dead(e) { if (e.key === 'Dead') { e.stopImmediatePropagation(); e.preventDefault(); return true; } return false; }
      window.addEventListener('keydown', function (e) {
        if (dead(e)) return;
        if (e.ctrlKey && /^(Digit[1-9]|Numpad[1-9]|KeyQ)$/.test(e.code)) e.preventDefault();
      }, true);
      window.addEventListener('keyup', dead, true);
    })();
    </script>
</head>"""
rep('\n</head>', KEYS)
open(out, 'w', encoding='utf-8').write(t)
