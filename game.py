from human import Human
from computer import Computer

class Game:
    def __init__(self):
        self.gestures_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.players_list = []

    def welcome(self):
        print ("____________________________________________________")
        print (" ")
        print ("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print ("____________________________________________________")
        print ("Rules: ")
        print (" ")
        print ("Rock crushes Scissors")
        print ("Scissors cuts Paper")
        print ("Paper covers Rock")
        print ("Rock crushes Lizard")
        print ("Lizard poisons Spock")
        print ("Spock smashes Scissors")
        print ("Scissors decapitates Lizard")
        print ("Lizard eats Paper")
        print ("Paper disproves Spock")
        print ("Spock vaporizes Roc")
        print (" ")
        self.choose_Players()


    def choose_Players(self):
        print ("____________________________________________________")
        print (" ")
        num_check = False
        while num_check == False:
            num_input = input ("How many players?: ")
            if num_input == "1":
                num_check = True
                print ("One player.")
                self.create_players(1)
            elif num_input == "2":
                print ("Two players.")
                num_check = True
                self.create_players(2)
            else:
                print ("Invalid option. Try again.")
                self.choose_Players()
        
    def create_players(self, number_of_players):
        if number_of_players == 1:
            player1 = Human()
            player2 = Computer()
            self.players_list.append(player1)
            self.players_list.append(player2)
            self.start_game()
        else:
            player1 = Human()
            player2 = Human()
            self.players_list.append(player1)
            self.players_list.append(player2)
            self.start_game()

    def start_game(self):
        player1 = self.players_list[0]
        player2 = self.players_list[1]
        player1.choose_gesture(self.gestures_list)
        player2.choose_gesture(self.gestures_list)
        self.compare(player1, player2)

    def compare(self, player1, player2):
        if (player1.gesture == player2.gesture):
            print ("Draw")
        elif (player1.gesture == "Rock") and (player2.gesture == "Sc")

    def declare_winner(self, winner):
        pass