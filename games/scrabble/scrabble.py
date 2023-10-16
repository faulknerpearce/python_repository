letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

zipped = zip(letters, points)

points_map = {key: value for key, value in zipped}

# Add another key: and value to our dictionary. 
points_map[" "] = 0

# This function will return a score from a provided word. This word is scored from the mapped points in the letters dictionary. 
def score_word(word, dictionary):
    points_total = 0
    for letter in word:
        # Convert all letters to uppercase so they are scored corectly. 
        cap_letter = letter.upper()
        points_total += dictionary.get(cap_letter, 0)
    return points_total
      
player_group = {
    "player1": {1: "BLUE", 2: "TENNIS", 3: "EXIT"}, 
    "wordNerd": {1: "EARTH", 2: "EYES", 3: "MACHINE"},
    "Lexi Con": {1: "ERASER", 2: "BELLY", 3: "HUSKY"}, 
    "Prof Reader": {1: "ZAP", 2: "COMA", 3: "PERIOD"}
}
# This function will return the players total score for their played words. 
def get_player_score(name, profiles, dictionary):
    i = 1
    player_points = 0 
    while i <= len(profiles[name]):
        word = profiles[name].get(i, 0)
        player_points += score_word(word, dictionary)
        i += 1
    return player_points
        
# This sould result in a map of the names of the players and their scores.      
player_to_points = {}

for player in player_group:
    player_points = get_player_score(player, player_group, points_map)
    player_to_points[player] = player_points

def play_another_word(word, player, profiles, dictionary):
    profiles[player] += score_word(word, dictionary)
    return profiles

print(player_points)
    
