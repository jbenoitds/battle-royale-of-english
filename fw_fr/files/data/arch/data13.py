# Sample data structure for a quest

data_all_else = {
    # Data ID
    'data_id': 1102,
    'quest_title': "L'Attaque des Pirates : Le Parc Perdu",

    # Number of Enemies
    'enemy_spots': 3,

    # ID of Boss
    'boss': "pi1",  # Jack Sparrow

    # ID of Enemies
    'enemy1': "pi2",  # random pirate 1
    'enemy2': "pi3",  # random pirate 2
    'enemy3': "pi5",  # Skeleton pirate

    # Enemy Group
    'enemy_group': "pi",  # Pirates

    # Special Location
    'specloc': "pirateparc",  # Pirate-themed children park

    # Valid Items
    'item1': "compass",  # Ensure it's from the items list
    'item2': "map",  # Ensure it's from the items list
    'item1fake': "battery",  # Ensure it's from the items list
    'item2fake': "knife",  # Ensure it's from the items list

    # Zone for the quest
    'zone': "parc",  # Ensure it's from the zones list

    # Tag (should be a valid tag)
    'tag': "adventure",  # Make sure it's from the acceptable tags

    # Positions (ensure the coordinates are within the valid range of 50 to 450)
    'position': (150, 350),  # Example coordinates
}

# Additional quests can be generated similarly, adjusting the parameters as needed.

data_all_else2 = {
    'data_id': 1103,
    'quest_title': "Le Duel des Avengers : La Bataille de la Rue",

    'enemy_spots': 3,

    'boss': "av6",  # Thor

    'enemy1': "av1",  # Hulk
    'enemy2': "av4",  # Black Panther
    'enemy3': "av5",  # Ironman

    'enemy_group': "av",  # Avengers

    'specloc': "fire",  # Fire station

    'item1': "hammer",  # Ensure it's from the items list
    'item2': "wrist_watch",  # Ensure it's from the items list
    'item1fake': "lantern",  # Ensure it's from the items list
    'item2fake': "old_clock",  # Ensure it's from the items list

    'zone': "neighbor",  # Ensure it's from the zones list

    'tag': "battle",  # Ensure it's from the acceptable tags

    'position': (200, 300),  # Example coordinates
}

# Continue generating more quests as needed.
