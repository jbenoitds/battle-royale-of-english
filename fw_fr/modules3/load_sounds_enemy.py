import os
import pygame
from modules3.soundfix import load_sound

def load_sounds_enemy(sound_folder):
    # List of sound files for each set
    sound_files1 = ["11.mp3", "12.mp3", "13.mp3", "14.mp3"]
    sound_files2 = ["21.mp3", "22.mp3", "23.mp3", "24.mp3"]
    sound_files3 = ["31.mp3", "32.mp3", "33.mp3", "34.mp3"]
    sound_files4 = ["41.mp3", "42.mp3", "43.mp3", "44.mp3"]
    sound_files5 = ["51.mp3", "52.mp3", "53.mp3", "54.mp3"]
    sound_files6 = ["61.mp3", "62.mp3", "63.mp3", "64.mp3"]
    # Kakachi (enemy 7). The files 71-74.mp3 are now Everest's (the dog of the Ultimate Mission),
    # so level 3 uses the original Kakachi copies 71kakachi-74kakachi.mp3 (keys stay '71'-'74').
    sound_files7 = ["71kakachi.mp3", "72kakachi.mp3", "73kakachi.mp3", "74kakachi.mp3"]


    # Function to load sounds into a dictionary
    def load_sounds(sound_files):
        sound_dict = {}
        for sound_file in sound_files:
            sound_path = os.path.join(sound_folder, sound_file)  # Construct full file path
            sound_name = os.path.splitext(sound_file)[0].replace('kakachi', '')  # File name without extension (e.g. '71')
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


'''
def load_sounds_enemy(sound_folder, sound_keys):
    """
    Load sounds from a specified folder and store them in a dictionary.

    Args:
    sound_folder (str): Path to the folder containing sounds.
    sound_keys (list): List of sound file keys to load (without extension).

    Returns:
    dict: Dictionary containing three sub-dictionaries with sound keys and loaded sounds.
    """
    # Initialize the sub-dictionaries
    sub_sound_dict1 = {}
    sub_sound_dict2 = {}
    sub_sound_dict3 = {}
    
    # Load the sounds into the appropriate sub-dictionaries
    for key in sound_keys:
        filename = f"{key}.mp3"
        sound_path = os.path.join(sound_folder, filename)
        sound = load_sound(sound_path)
        
        if key.startswith('1'):
            sub_sound_dict1[key] = sound
        elif key.startswith('2'):
            sub_sound_dict2[key] = sound
        elif key.startswith('3'):
            sub_sound_dict3[key] = sound

    # Combine the sub-dictionaries into the main sound_dict
    sound_dict = {
        'sub_sound_dict1': sub_sound_dict1,
        'sub_sound_dict2': sub_sound_dict2,
        'sub_sound_dict3': sub_sound_dict3
    }

    return sound_dict
    '''