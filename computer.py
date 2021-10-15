from player import Player

class Computer(Player):
    def __init__(self):
        self.name = "Computer"
        super().__init__()

    def choose_gesture(self, gestures):
        pass