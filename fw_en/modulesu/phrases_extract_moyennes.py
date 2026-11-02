import random

def moyennes_phrases(unpack, file_path, number_phrases, number_per):

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
    if unpack == 16:
        sub_dicts = {
            'phrase1_dict': {}, 'phrase2_dict': {}, 'phrase3_dict': {}, 'phrase4_dict': {},
            'phrase5_dict': {}, 'phrase6_dict': {}, 'phrase7_dict': {}, 'phrase8_dict': {},
            'phrase9_dict': {}, 'phrase10_dict': {}, 'phrase11_dict': {}, 'phrase12_dict': {},
            'phrase13_dict': {}, 'phrase14_dict': {}, 'phrase15_dict': {}, 'phrase16_dict': {}
            }
    elif unpack == 4:
        sub_dicts = {
            'phrase1_dict': {}, 'phrase2_dict': {}, 'phrase3_dict': {}, 'phrase4_dict': {},
            }

    # Distribute remaining phrases into sub-dictionaries
    for n in range(unpack):
        start_index = number_per * n
        
        for i in range(number_per):
            index = start_index + i
            if index < number_phrases:
                phrase_key = f'phrase{i + 1}'
                                
                sub_dicts[f'phrase{n + 1}_dict'][phrase_key] = selected_lines[index]

    # Return all sub-dictionaries in a tuple
    if unpack == 16:        
        return (sub_dicts['phrase1_dict'], sub_dicts['phrase2_dict'], sub_dicts['phrase3_dict'],
                sub_dicts['phrase4_dict'], sub_dicts['phrase5_dict'], sub_dicts['phrase6_dict'],
                sub_dicts['phrase7_dict'], sub_dicts['phrase8_dict'], sub_dicts['phrase9_dict'],
                sub_dicts['phrase10_dict'], sub_dicts['phrase11_dict'], sub_dicts['phrase12_dict'],
                sub_dicts['phrase13_dict'], sub_dicts['phrase14_dict'], sub_dicts['phrase15_dict'],
                sub_dicts['phrase16_dict'])
    
    elif unpack == 4:        
        return (sub_dicts['phrase1_dict'], sub_dicts['phrase2_dict'], sub_dicts['phrase3_dict'],
                sub_dicts['phrase4_dict'])