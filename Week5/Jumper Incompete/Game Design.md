# cse210-2
 Team Work
# Jumper
Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.
# Rules
Jumper is played according to the following rules.

The puzzle is a secret word randomly chosen from a list.
The player guesses a letter in the puzzle.
If the guess is correct, the letter is revealed.
If the guess is incorrect, a line is cut on the player's parachute.
If the puzzle is solved the game is over.
If the player has no more parachute the game is over.

## Game Design

Class: Jumper 
---
_textline: [] (private attribute)
---
get_file():None
set_file():None
---


Class: Player
---

---

---


Class: Director
---
_jumper = Jumper() (private attribute)
_is_playing = True (private attribute)
_secret = Secret() (private attribute)
_player = Player() (private attribute)
---
start_game():None
get_prompt():None
do_updates():None
---

Class: Secret
---
_secret: str (private attribute)
---
get_file():None
set_file():None
---

Text: File
---
Contains text for random word
---

Text: File
---
Contains text to display parachute
---

Function: main
---
Starts game.
---