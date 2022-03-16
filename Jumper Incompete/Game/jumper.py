

class Jumper:
    def __init__(self, ):
        self._alive = "O"
        self._line_1 = "  ___"
        self._line_2 = "/ ___ \ "
        self._line_3 = "\     /"
        self._line_4 = " \   /"
        self._line_5 = "   "
        self._line_6 = "  /|\ "
        self._line_7 = "  / \ "
        self._line_8 = "⌃⌃⌃⌃⌃⌃⌃"


    def get_alive(self):
        self._alive = "x"

    def display(self, number):
        self.check = number
        if self.check == 4:
            print(self._line_1)
            print(self._line_2)
            print(self._line_3)
            print(self._line_4)
            print(self._line_5 + self._alive)
            print(self._line_6)
            print(self._line_7)
            print("")
            print(self._line_8)
        if self.check == 3:
            print(self._line_2)
            print(self._line_3)
            print(self._line_4)
            print(self._line_5 + self._alive)
            print(self._line_6)
            print(self._line_7)
            print("")
            print(self._line_8)
        if self.check == 2:
            print(self._line_3)
            print(self._line_4)
            print(self._line_5 + self._alive)
            print(self._line_6)
            print(self._line_7)
            print("")
            print(self._line_8)
        if self.check == 1:
            print(self._line_4)
            print(self._line_5 + self._alive)
            print(self._line_6)
            print(self._line_7)
            print("")
            print(self._line_8)
        else:
            self.get_alive()
            print(self._line_5 + self._alive)
            print(self._line_6)
            print(self._line_7)
            print("")
            print(self._line_8)

    def update(self):
        return 1
