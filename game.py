class Game:
    def __init__(self):
        self.gestures_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

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
            elif num_input == "2":
                print ("Two players.")
                num_check = True
            else:
                print ("Invalid option. Try again.")
                self.choose_Players()
        
        

    def create_players(self):
        pass

    def start_game(self):
        pass

    def compare(self, player1, player2):
        pass

    def declare_winner(self, winner):
        pass