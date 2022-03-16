

class Player:
    """
    Keeps track of the players guessed letters and adds correct guesses into display
    """
    def __init__(self):
        self.word = []

    def create_word(self, number):
        """
        Creates the array from the number of letters in the secret
        """
        i = number
        while i > -1:
            self.word[i] = "_"
            i -= 1

    def display(self):
        """
        Displays the word array
        """
        iw = 0
        for iw in self._word:
            print(f"{self._word[iw]} ")

    def update(self, index, letter):
        """
        Updates opsition with the player guess
        """
        self.word[index] = letter