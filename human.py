from player import Player

class Human(Player):
    def __init__(self):
        self.name = self.choose_name()
        super().__init__()

    def choose_gesture(self, gestures):
        print("Choose your gesture: ")
        for gesture in gestures:
            print(f"{gestures.index(gesture) + 1} - {gesture}")
        i = int(input()) - 1
        self.current_gesture = gestures[i]
        

    def choose_name(self):
        name = input(f"Enter players's name: ")
        return name