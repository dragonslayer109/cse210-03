from Game.secret import Secret 
from Game.player import Player
from Game.player import Jumper
class Director:
    """
    Directs the gameplay of the game
    """
    def __init__(self):
        self._secret = ""
        self.secrets = Secret()
        self._is_playing = True
        self._player_word = ""
        self.player = Player()
        self.guess = ""
        self.jumper = Jumper()
        self.lives = 0

    
    def start_game(self):
        """
        Initialises the start of the game and runs it
        """
        self.lives = 4
        self.get_secret()
        while self._is_playing == True:
            self.get_prompt()
            self.do_updates()
   
    def get_secret(self):
        """
        Get the secret word for secret class
        """
        self._secret = self.secrets.get_word
    
    def set_playing(self):
        """
        sets alive to False
        """
        self._is_playing == False

    def get_prompt(self):
        """
        Get user prompts
        """
        if not self._is_playing:
            return 
        self.player.display #will change based on player calls made
        self.jumper.display #will change based on jumper calls made
        self.guess = input("Guess a letter [a-z]: ")

    def do_updates(self):
        """
        Update the player against secret and update parachute
        If the guess is correct replace the players index number 
        with the new value.
        If the guess is incorrect, remove the first index line from display
        Check for full word guessed as player
        Check for 4 incorrect guesses.
        """
        if not self._is_playing:
            return 
        for i in self._secret:
            if self.guess == self._secret:
                self.player.update #will change based on player calls made
            else:
                self.jumper.update #will change based on jumper calls made
                self.lives -= 1
                if self.lives == 0:
                    self.set_playing()
                
