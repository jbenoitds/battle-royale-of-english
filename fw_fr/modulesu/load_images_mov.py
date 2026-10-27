import pygame

### Function to load images based on the spots and orientations
# !!! ADJUST
def load_images_mov(num_spots, num_orientations):
    images = {}
    for spot in range(1, 12):
        for orientation in range(1, num_orientations + 1):
            key = f"{spot}_{orientation}"
            try:
                images[key] = pygame.image.load(f'files/background/missionu/{key}.jpg')
            except FileNotFoundError:
                print(f"Erreur: Fichier image 'files/background/missionu/{key}.jpg' non trouvé.")
                images[key] = None  # Assign None or a placeholder image

    for spot in range(21, 23):
        for orientation in range(1, num_orientations + 1):
            key = f"{spot}_{orientation}"
            try:
                images[key] = pygame.image.load(f'files/background/missionu/{key}.jpg')
            except FileNotFoundError:
                print(f"Erreur: Fichier image 'files/background/missionu/{key}.jpg' non trouvé.")
                images[key] = None  # Assign None or a placeholder image

    for spot in range(31, 41):
        for orientation in range(1, num_orientations + 1):
            key = f"{spot}_{orientation}"
            try:
                images[key] = pygame.image.load(f'files/background/missionu/{key}.jpg')
            except FileNotFoundError:
                print(f"Erreur: Fichier image 'files/background/missionu/{key}.jpg' non trouvé.")
                images[key] = None  # Assign None or a placeholder image

    for spot in range(51, 55):
        for orientation in range(1, num_orientations + 1):
            key = f"{spot}_{orientation}"
            try:
                images[key] = pygame.image.load(f'files/background/missionu/{key}.jpg')
            except FileNotFoundError:
                print(f"Erreur: Fichier image 'files/background/missionu/{key}.jpg' non trouvé.")
                images[key] = None  # Assign None or a placeholder image

    for spot in range(61, 69):
        for orientation in range(1, num_orientations + 1):
            key = f"{spot}_{orientation}"
            try:
                images[key] = pygame.image.load(f'files/background/missionu/{key}.jpg')
            except FileNotFoundError:
                print(f"Erreur: Fichier image 'files/background/missionu/{key}.jpg' non trouvé.")
                images[key] = None  # Assign None or a placeholder image

    for spot in range(71, 80):
        for orientation in range(1, num_orientations + 1):
            key = f"{spot}_{orientation}"
            try:
                images[key] = pygame.image.load(f'files/background/missionu/{key}.jpg')
            except FileNotFoundError:
                print(f"Erreur: Fichier image 'files/background/missionu/{key}.jpg' non trouvé.")
                images[key] = None  # Assign None or a placeholder image

    for spot in range(81, 92):
        for orientation in range(1, num_orientations + 1):
            key = f"{spot}_{orientation}"
            try:
                images[key] = pygame.image.load(f'files/background/missionu/{key}.jpg')
            except FileNotFoundError:
                print(f"Erreur: Fichier image 'files/background/missionu/{key}.jpg' non trouvé.")
                images[key] = None  # Assign None or a placeholder image

    return images