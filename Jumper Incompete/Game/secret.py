import random
class Secret:
    """
    Reads from a file and returns a random word 
    """
    def __init__(self):
        self._words = ""
    
    def get_word(self):
        self._words = "write short answer question submit learn times anytime course your mastery "
        self._words = list(map(str, self._words.split()))
        return random.choice(self._words)