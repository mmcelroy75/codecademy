letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#15.3 - To include lower-case inputs:
for x in range(len(letters)):
  letters.append(letters[x].lower())
for i in range(len(points)):
  points.append(points[i])

letters_to_points = {letters: points for letters, points in zip(letters,points)}

letters_to_points[""] = 0
#print(letters_to_points)

def score_word(word):
  point_total = 0
  for x in word:
    if x in letters_to_points.keys():
      point_total += letters_to_points.get(x,0)
  return point_total

player_to_points = {}

#15.2 - Update Point Totals
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
      player_to_points.update({player:player_points})
  return player_to_points

#brownie_points = score_word("BROWNIE")

#print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["eraser", "BELLY", "husky"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

#15.1 - play_word function
def play_word(player, word):
  if player in player_to_words.keys():
    player_to_words[player].append(word)
  else:
    player_to_words.update({player: [word]})
  
  update_point_totals()
  print(player_to_points)

  
play_word("player1", "Egress")
play_word("Jimmy", "Underneath")
play_word("Lexi Con", "BARBER")

print(player_to_words)
