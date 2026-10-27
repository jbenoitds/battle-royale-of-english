import os
import pygame
from modules3.soundfix import load_sound

def load_sounds(folder_path):
    sound_dict = {}
    
    # Ensure pygame.mixer is initialized
    pygame.mixer.init()
    
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter sound files (adjust extensions as needed)
    sound_files = [f for f in files if f.endswith('.mp3')]
    
    for filename in sound_files:
        # Remove extension to get the key
        name_without_extension = os.path.splitext(filename)[0]
        
        # Construct full file path
        file_path = os.path.join(folder_path, filename)
        
        # Load sound and store in dictionary
        sound_dict[name_without_extension] = load_sound(file_path)
    
    return sound_dict