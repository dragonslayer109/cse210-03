import random
class Secret:
    """
    Reads from a file and returns a random word 
    """
    def __init__(self):
        self._text = ""
        self._words = ""
    
    def get_word(self):
        with open(".Text/Words.txt", "r") as file:
            self._text = file.read()
            self._words = list(map(str, self._text.split()))
            return random.choice(self._words)