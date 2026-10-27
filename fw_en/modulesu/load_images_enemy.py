import os
import pygame

class ImageLoaderEnemy:
    def __init__(self, folder):
        self.folder = folder
        self.load_images_enemy()

    def load_images_enemy(self):
        # Ensure pygame is initialized
        pygame.init()

        self.images = {}

        # Iterate over all files in the folder
        for filename in os.listdir(self.folder):
            # Check if the file is an image file
            if filename.lower().endswith(('.png', '.jpg', '.JPG', '.jpeg')):
                # Construct the full file path
                file_path = os.path.join(self.folder, filename)

                # Load the image
                image = pygame.image.load(file_path).convert_alpha()

                # Remove the file extension to get the variable name
                var_name = os.path.splitext(filename)[0]

                # Store the image in the instance's dictionary
                self.images[var_name] = image

    def get_enemy(self, name):
        # Retrieve an image by name
        if name in self.images:
            return self.images[name]
        else:
            raise ValueError(f"Image '{name}' not found in the specified folder.")