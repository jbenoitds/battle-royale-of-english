import pygame

### Function to load images based on the spots and orientations
# !!! ADJUST
def load_images_mov(num_spots, num_orientations):
    images = {}
    for spot in range(1, num_spots + 1):
        for orientation in range(1, num_orientations + 1):
            key = f"{spot}_{orientation}"
            try:
                images[key] = pygame.image.load(f'files/background/mission3/{key}.png')
            except FileNotFoundError:
                print(f"Erreur: Fichier image 'files/background/mission3/{key}.png' non trouvé.")
                images[key] = None  # Assign None or a placeholder image

    return images