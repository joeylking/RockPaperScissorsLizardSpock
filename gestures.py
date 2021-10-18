class Gesture:
    def __init__(self, name):
        self.name = name
        self.loses_to = []

    def compare(self, other_gesture):
        for i in self.loses_to:
            if i == other_gesture:
                return 0
            