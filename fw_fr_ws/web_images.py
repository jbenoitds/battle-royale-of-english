"""Web version, step 2b of build_web.sh: pictures.
1. big opaque PNG pictures -> JPG (mission 2/3 backgrounds, loader...): 140 MB -> ~20 MB;
   the code is updated to the new file names.
2. level backgrounds (mission2/3/u) are loaded only when shown (weblazy.py).
usage: python web_images.py STAGE_DIR"""
import sys, os, re, glob
from PIL import Image

root = sys.argv[1]
os.chdir(root)
converted, kept = set(), {}
for f in glob.glob('files/**/*.png', recursive=True):
    d = os.path.dirname(f)
    kept.setdefault(d, 0)
    im = Image.open(f)
    opaque = True
    if im.mode in ('RGBA', 'LA', 'P', 'PA'):
        opaque = im.convert('RGBA').getchannel('A').getextrema()[0] == 255
    if opaque and os.path.getsize(f) > 200_000:
        im.convert('RGB').save(f[:-4] + '.jpg', 'JPEG', quality=85, optimize=True)
        os.remove(f)
        converted.add(f.replace('\\', '/'))
    else:
        kept[d] += 1
# big JPG photos (Street View, menu...) re-saved lighter when it saves at least 25 %
saved = 0
for f in glob.glob('files/**/*.jpg', recursive=True):
    if f.replace('\\', '/') in {c[:-4] + '.jpg' for c in converted} or os.path.getsize(f) < 150_000:
        continue
    before = os.path.getsize(f)
    im = Image.open(f).convert('RGB')
    im.save(f + '.tmp', 'JPEG', quality=82, optimize=True)
    if os.path.getsize(f + '.tmp') < 0.75 * before:
        saved += before - os.path.getsize(f + '.tmp')
        os.replace(f + '.tmp', f)
    else:
        os.remove(f + '.tmp')
print(f'JPG photos re-saved lighter: {saved / 1e6:.1f} MB saved')
full_dirs = {d.replace('\\', '/') for d, n in kept.items() if n == 0}
print(f'{len(converted)} PNG -> JPG; whole folders: {sorted(full_dirs)}')

code = glob.glob('*.py') + glob.glob('modules*/*.py')
for p in code:
    s = open(p, encoding='utf-8').read()
    new = s
    for f in converted:
        new = new.replace(f, f[:-4] + '.jpg')
    for d in full_dirs:
        new = re.sub(r"(%s/[^'\"\n]*?)\.png" % re.escape(d), r'\1.jpg', new)
    if new != s:
        open(p, 'w', encoding='utf-8').write(new)
        print('  file names updated in', p)

LOADERS = ['modules2/load_images.py', 'modules3/load_images_mov.py', 'modulesu/load_images_mov.py']
for p in LOADERS:
    s = open(p, encoding='utf-8').read()
    assert 'images = {}' in s and "pygame.image.load(f'files/background/" in s, p
    s = s.replace('images = {}', 'images = LazyImages()')
    s = s.replace("pygame.image.load(f'files/background/", "lazy_path(f'files/background/")
    s = s.replace('import pygame\n', 'import pygame\nfrom weblazy import LazyImages, lazy_path  # web: load when shown\n', 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('  lazy loading in', p)
