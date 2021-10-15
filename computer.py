from player import Player
import random

class Computer(Player):
    def __init__(self):
        self.name = "Computer"
        super().__init__()

    def choose_gesture(self, gestures):
        i = random.randint(0, len(gestures) -1)
        self.current_gesture = gestures[i]
        print(f"The computer has chosen {gestures[i]}")