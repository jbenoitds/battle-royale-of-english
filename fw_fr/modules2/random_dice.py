import random

def random_dice():
    """
    Creates a dictionary that maps 0, 1, 2 to a random permutation of 0, 1, 2
    ensuring each mapping is unique.

    Returns:
    dict: A dictionary with keys 0, 1, 2 and values as a random permutation of 0, 1, 2
    """
    keys = [1, 2, 3]
    values = [1, 2, 3]
    random.shuffle(values)
    return dict(zip(keys, values))
