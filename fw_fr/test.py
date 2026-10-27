sco_list = [(4,5),(4,4)]
search_spots_orientations = [(2,3),(4,5),(4,4)]
saved_game = 'y'

search_challenge_conditions = {}

for location in search_spots_orientations:
    search_challenge_conditions[location] = True

print(search_challenge_conditions)

# Update search_challenge_conditions based on save
if saved_game == 'y':
    for location in search_spots_orientations:
        if location in sco_list:
            search_challenge_conditions[location] = False

print(search_challenge_conditions)