# Web version: level backgrounds are loaded only when they are shown (a browser tab has
# much less memory than a PC: level 4 alone has 220 photos = ~700 MB once loaded).
# The last MAX_LOADED pictures stay in memory, so going back and forth stays fast.
import os
import collections
import pygame

MAX_LOADED = 40


class LazyImages(dict):
    def __init__(self):
        super().__init__()
        self._loaded = collections.OrderedDict()

    def __getitem__(self, key):
        path = dict.__getitem__(self, key)
        if not isinstance(path, str):
            return path  # None (missing picture) or already a picture
        if key in self._loaded:
            self._loaded.move_to_end(key)
            return self._loaded[key]
        picture = pygame.image.load(path)
        self._loaded[key] = picture
        if len(self._loaded) > MAX_LOADED:
            self._loaded.popitem(last=False)
        return picture

    def get(self, key, default=None):
        return self[key] if key in self else default


def lazy_path(path):
    """Like pygame.image.load(path) for a LazyImages dict: only checks that the file exists."""
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    return path
