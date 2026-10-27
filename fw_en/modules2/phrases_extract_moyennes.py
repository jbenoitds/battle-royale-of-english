import random

def moyennes_phrases(file_path, number_phrases):

    # Open the file in read mode with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read all lines into a list
        # ignore empty lines (an empty line would be an impossible sentence)
        lines = [line for line in file.readlines() if line.strip()]

    # If the number of phrases requested is more than the available lines, adjust accordingly
    if number_phrases > len(lines):
        print(f"Requested {number_phrases} phrases, but only {len(lines)} lines are available.")
        number_phrases = len(lines)

    # Randomly select the specified number of unique lines
    selected_lines = random.sample(lines, number_phrases)

    # Strip whitespace from selected lines
    # lower case, straight apostrophes, single spaces: what the player can actually type
    selected_lines = [' '.join(line.replace('\u2019', "'").split()).lower() for line in selected_lines]

    # Initialize dictionaries to store original and quoted phrases
    phrase_dict = {}

    # Store the selected lines in dictionaries
    for i in range(number_phrases):
        key = f'phrase{i + 1}'
        phrase_dict[key] = selected_lines[i]

    # Initialize sub-dictionaries
    sub_dicts = {'special_dict': {}}

    # Fill special_dict with phrases 1, 2, and 3
    for i in range(3):
        special_key = f'phrase{i + 1}'
        sub_dicts['special_dict'][special_key] = selected_lines[i]

    # Return all sub-dictionaries in a tuple
    return (sub_dicts['special_dict'])