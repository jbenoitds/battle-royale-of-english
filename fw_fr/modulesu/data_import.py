import os
import random
import importlib.util

PLAYED_FILE = 'files/saves/quests_played.txt'


def _read_played():
    try:
        with open(PLAYED_FILE, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except OSError:
        return []


def _write_played(names):
    try:
        with open(PLAYED_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(names) + '\n')
    except OSError:
        pass


def _load_module(directory, file_name):
    module_name = file_name[:-3]  # Remove the '.py' extension
    spec = importlib.util.spec_from_file_location(module_name, os.path.join(directory, file_name))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, 'data_all'):
        raise AttributeError(f"The module {module_name} does not contain 'data_all'.")
    return getattr(module, 'data_all')


def list_quests(directory='files/data'):
    """All the quests, in file-name order: [(letter, file name, title), ...].
    The menu shows them; '4a' plays the first one, '4b' the second one, etc."""
    py_files = sorted(f for f in os.listdir(directory) if f.endswith('.py'))
    quests = []
    for i, file_name in enumerate(py_files[:26]):
        try:
            title = _load_module(directory, file_name).get('quest_title', file_name)
        except Exception:
            continue  # a broken quest file is simply not listed
        quests.append((chr(ord('a') + i), file_name, title))
    return quests


def import_quest(directory, file_name):
    """Load one chosen quest (menu '4a', '4b'...). It also counts as played for the shuffle."""
    played = _read_played()
    if file_name in played:
        played.remove(file_name)
    _write_played(played + [file_name])
    return _load_module(directory, file_name)


def import_data_all(directory):
    """Pick the quest of the Ultimate Mission like a shuffled deck of cards:
    every quest file (files/data/*.py) is played once, in a random order, before any
    quest comes back, and the same quest is never played twice in a row."""
    py_files = sorted(f for f in os.listdir(directory) if f.endswith('.py'))

    if not py_files:
        raise ValueError("No .py files found in the specified directory.")

    played = [p for p in _read_played() if p in py_files]
    remaining = [f for f in py_files if f not in played]
    if not remaining:  # every quest was played: new round, but not the last one again
        last = played[-1] if played else None
        played = []
        remaining = [f for f in py_files if f != last] or py_files
    random_file = random.choice(remaining)
    _write_played(played + [random_file])

    random_file_path = os.path.join(directory, random_file)

    # Import the module from the chosen file
    module_name = random_file[:-3]  # Remove the '.py' extension
    spec = importlib.util.spec_from_file_location(module_name, random_file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get the data_all dictionary from the module
    if not hasattr(module, 'data_all'):
        raise AttributeError(f"The module {module_name} does not contain 'data_all'.")

    return getattr(module, 'data_all')
