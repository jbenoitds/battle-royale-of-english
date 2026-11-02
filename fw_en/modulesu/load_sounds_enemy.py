import os
import pygame
from modulesu.soundfix import load_sound

def load_sounds_enemy(sound_folder, tag1, tag2, tag3, tag4, tag5, tagboss, tageverest):
    sound_files1 = [f"{tag1}1.mp3", f"{tag1}2.mp3", f"{tag1}3.mp3", f"{tag1}4.mp3"]
    sound_files2 = [f"{tag2}1.mp3", f"{tag2}2.mp3", f"{tag2}3.mp3", f"{tag2}4.mp3"]
    sound_files3 = [f"{tag3}1.mp3", f"{tag3}2.mp3", f"{tag3}3.mp3", f"{tag3}4.mp3"]
    sound_files4 = [f"{tag4}1.mp3", f"{tag4}2.mp3", f"{tag4}3.mp3", f"{tag4}4.mp3"]
    sound_files5 = [f"{tag5}1.mp3", f"{tag5}2.mp3", f"{tag5}3.mp3", f"{tag5}4.mp3"]
    sound_files6 = [f"{tagboss}1.mp3", f"{tagboss}2.mp3", f"{tagboss}3.mp3", f"{tagboss}4.mp3"]
    sound_files7 = [f"{tageverest}1.mp3", f"{tageverest}2.mp3", f"{tageverest}3.mp3", f"{tageverest}4.mp3"]
    
    # Function to load sounds into a dictionary
    def load_sounds(sound_files):
        sound_dict = {}
        for sound_file in sound_files:
            sound_path = os.path.join(sound_folder, sound_file)  # Construct full file path
            sound_name = os.path.splitext(sound_file)[0]  # Extract file name without extension
            sound = load_sound(sound_path)
            sound_dict[sound_name] = sound
        return sound_dict

    # Load sounds for each set

    sound_dict1 = load_sounds(sound_files1)
    sound_dict2 = load_sounds(sound_files2)
    sound_dict3 = load_sounds(sound_files3)
    sound_dict4 = load_sounds(sound_files4)
    sound_dict5 = load_sounds(sound_files5)
    sound_dict6 = load_sounds(sound_files6)
    sound_dict7 = load_sounds(sound_files7)


    
    return sound_dict1, sound_dict2, sound_dict3, sound_dict4, sound_dict5, sound_dict6, sound_dict7