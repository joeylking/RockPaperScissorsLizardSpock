from player import Player

class Human(Player):
    def __init__(self):
        self.name = self.choose_name()
        super().__init__()

    def choose_gesture(self, gestures):
        print (" ")
        print("Choose your gesture: ")
        loop = True
        while loop == True:
            for gesture in gestures:
                print(f"{gestures.index(gesture) + 1} - {gesture}")
            i = int(input()) - 1
            if i >= 0 and i < len(gestures):
                loop = False
                self.gesture = gestures[i]
            else:
                input("Invalid choice. Try again: ")
        
    def choose_name(self):
        print (" ")
        name = input(f"Enter players's name: ")
        return name