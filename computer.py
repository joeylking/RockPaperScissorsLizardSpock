from player import Player
import random

class Computer(Player):
    def __init__(self):
        self.name = "Computer"
        super().__init__()

    def choose_gesture(self, gestures):
        self.gesture = random.choice(gestures)
        print (" ")
        print(f"The computer has chosen {self.gesture.name}")
