from human import Human
from computer import Computer

class Game:
    def __init__(self):
        self.gestures_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.players_list = []
        self.welcome()

    def welcome(self):
        print (50 * "*")
        print (" ")
        print ("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print (" ")
        print (50 * "*")
        print (" ")
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
        print ("Spock vaporizes Rock")
        print (" ")
        print ("Best out of 3 wins!")
        print (" ")
        self.choose_players()


    def choose_players(self):
        print (50 * "-")
        print (" ")
        num_check = False
        while num_check == False:
            num_input = input ("How many players? ")
            if num_input == "1":
                num_check = True
                print ("One player chosen.")
                self.create_players(1)
            elif num_input == "2":
                print ("Two players chosen.")
                num_check = True
                self.create_players(2)
            else:
                print ("Invalid option. Try again.")
                self.choose_players()
        
    def create_players(self, number_of_players):
        if number_of_players == 1:
            player1 = Human()
            player2 = Computer()
            self.players_list.extend([player1, player2])
            self.start_game()
        else:
            player1 = Human()
            player2 = Human()
            self.players_list.extend([player1, player2])
            self.start_game()

    def start_game(self):
        player1 = self.players_list[0]
        player2 = self.players_list[1]
        print (50 * "-")
        print (" ")
        print(f"{player1.name} Vs. {player2.name}")
        print (" ")
        player1.choose_gesture(self.gestures_list)
        player2.choose_gesture(self.gestures_list)
        self.compare(player1, player2)

    def compare(self, player1, player2):
        print (" ")
        print (" ")
        if player1.gesture == player2.gesture:
            print ("Draw")
        elif player1.gesture == "Rock":
            if player2.gesture == "Scissors" or player2.gesture == "Lizard":
                print(f"{player1.name} crushes {player2.name}'s {player2.gesture} with a rock.")
                player1.wins += 1
            elif player2.gesture == "Paper":
                print(f"{player2.name} covers {player1.name}'s rock with paper.")
                player2.wins += 1
            elif player2.gesture == "Spock":
                print(f"{player2.name} vaporizes {player1.name}'s rock with Spock.")
                player2.wins += 1
        elif player1.gesture == "Scissors":
            if player2.gesture == "Paper":
                print(f"{player1.name} cuts {player2.name}'s paper with scissors.")
                player1.wins += 1
            elif player2.gesture == "Lizard":
                print(f"{player1.name} decapitates {player2.name}'s lizard with scissors.")
                player1.wins += 1
            elif player2.gesture == "Rock":
                print(f"{player2.name} crushes {player1.name}'s scissors with rock.")
                player2.wins += 1
            elif player2.gesture == "Spock":
                print(f"{player2.name} crushes {player1.name}'s scissors with Spock.")
                player2.wins += 1
        elif player1.gesture == "Paper":
            if player2.gesture == "Rock":
                print(f"{player1.name} covers {player2.name}'s rock with paper.")
                player1.wins += 1
            elif player2.gesture == "Spock":
                print(f"{player1.name} disproves {player2.name}'s Spock with a paper.")
                player1.wins += 1
            elif player2.gesture == "Scissors":
                print(f"{player2.name} cuts {player1.name}'s paper with scissors.")
                player2.wins += 1
            elif player2.gesture == "Lizard":
                print(f"{player2.name} eats {player1.name}'s paper with a lizard.")
                player2.wins += 1
        elif player1.gesture == "Lizard": 
            if player2.gesture == "Spock":
                print(f"{player1.name} poisons {player2.name}'s Spock with a lizard.")
                player1.wins += 1
            elif player2.gesture == "Paper":
                print(f"{player1.name} eats {player2.name}'s paper with a lizard.")
                player1.wins += 1
            elif player2.gesture == "Rock":
                print(f"{player2.name} crushes {player1.name}'s lizard with a rock.")
                player2.wins += 1
            elif player2.gesture == "Scissors":
                print(f"{player2.name} decapitates {player1.name}'s lizard with scissors.")
                player2.wins += 1
        elif player1.gesture == "Spock":
            if player2.gesture == "Scissors":
                print(f"{player1.name} smashes {player2.name}'s scissors with Spock.")
                player1.wins += 1
            elif player2.gesture == "Rock":
                print(f"{player1.name} vaporizes {player2.name}'s rock with Spock.")
                player1.wins += 1
            elif player2.gesture == "Paper":
                print(f"{player2.name} disproves {player1.name}'s Spock with a paper.")
                player2.wins += 1
            elif player2.gesture == "Lizard":
                print(f"{player2.name} poisons {player1.name}'s Spock with a lizard.")
                player2.wins += 1
        else:
            print ("error with comparing.")

        if player1.wins == 2:
                self.declare_winner(player1.name)
        elif player2.wins == 2:
            self.declare_winner(player2.name)
        else:
            player1.choose_gesture(self.gestures_list)
            player2.choose_gesture(self.gestures_list)
            self.compare(player1, player2)
            
    def declare_winner(self, winner):
        print (" ")
        print (50 * "!")
        print (" ")
        print(f"{winner} wins!")
        print (" ")
        print (50 * "-")
        exit()