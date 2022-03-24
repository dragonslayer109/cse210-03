

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
        self.word = ["_"] * number

    def display(self):
        """
        Displays the word array
        """
        for i in self.word:
            print(i, end=" ")
        print("\n")
 

    def update(self, index, letter):
        """
        Updates opsition with the player guess
        """
        self.word[index] = letter