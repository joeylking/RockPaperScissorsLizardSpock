from player import Player

class Human(Player):
    def __init__(self, player_number):
        self.player_number = player_number
        self.name = self.choose_name()
        super().__init__()

    def choose_gesture(self, gestures):
        print(f"\n{self.name}: Choose your gesture: ")
        loop = True
        while loop == True:
            for gesture in gestures:
                print(f"{gestures.index(gesture) + 1} - {gesture.name}")
            i = int(input()) - 1
            if i >= 0 and i < len(gestures):
                loop = False
                self.gesture = gestures[i]
            else:
                input("Invalid choice. Try again: ")
        
    def choose_name(self):
        name = input(f"\nEnter Player {self.player_number}'s name: ")
        return name