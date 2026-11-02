# Web version: the files in files/saves/ (level 4 save for 'go', quests already played) are
# copied into the browser's storage (localStorage) each time the game writes them, and put
# back when the page opens. Without this, closing the tab would forget them.
import builtins
import os
import platform  # pygbag's module: platform.window = the browser window

PREFIX = 'bataille_royale_fr:'
SAVE_DIR = 'files/saves/'
_real_open = builtins.open


def _key(path):
    rel = os.path.relpath(os.path.abspath(path)).replace('\\', '/')
    return rel if rel.startswith(SAVE_DIR) else None


def _store(rel):
    try:
        with _real_open(rel, 'r', encoding='utf-8') as f:
            platform.window.localStorage.setItem(PREFIX + rel, f.read())
    except Exception as e:
        print('websave: could not store', rel, e)


class _SavingFile:
    def __init__(self, f, rel):
        self._f, self._rel = f, rel

    def __getattr__(self, name):
        return getattr(self._f, name)

    def __iter__(self):
        return iter(self._f)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
        return False

    def close(self):
        if not self._f.closed:
            self._f.close()
            _store(self._rel)


def _open(file, mode='r', *args, **kwargs):
    f = _real_open(file, mode, *args, **kwargs)
    if isinstance(file, (str, os.PathLike)) and any(c in mode for c in 'wax+'):
        rel = _key(os.fspath(file))
        if rel:
            return _SavingFile(f, rel)
    return f


def restore():
    """Put the saved files back from the browser storage (called once at start)."""
    try:
        storage = platform.window.localStorage
        for i in range(int(storage.length)):
            k = str(storage.key(i))
            if k.startswith(PREFIX):
                rel = k[len(PREFIX):]
                os.makedirs(os.path.dirname(rel), exist_ok=True)
                with _real_open(rel, 'w', encoding='utf-8') as f:
                    f.write(str(storage.getItem(k)))
    except Exception as e:
        print('websave: could not restore', e)


restore()
builtins.open = _open
