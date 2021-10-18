from human import Human
from computer import Computer
from gestures import Gesture

class Game:
    def __init__(self):
        self.gestures_list = []
        self.players_list = []
        self.run()

    def run(self):
        self.welcome()
        number_of_players = self.choose_players()
        self.create_players(number_of_players)
        self.create_gestures()
        self.start_game()
        winner = self.compare(self.players_list[0], self.players_list[1])
        self.declare_winner(winner)

    def welcome(self):
        print (50 * "*")
        print (" ")
        print ("Welcome to Rock, Paper, Scissors, Lizard, Spock!\n")
        print (" ")
        print (50 * "*")
        print (" ")
        print ("Rules: ")
        print (" ")
        print ("Rock crushes Scissors")
        print ("Scissors cut Paper")
        print ("Paper covers Rock")
        print ("Rock crushes Lizard")
        print ("Lizard poisons Spock")
        print ("Spock smashes Scissors")
        print ("Scissors decapitate Lizard")
        print ("Lizard eats Paper")
        print ("Paper disproves Spock")
        print ("Spock vaporizes Rock")
        print (" ")
        print ("Best out of 3 wins!")
        print (" ")
        
    def create_gestures(self):
        rock = Gesture("Rock")
        paper = Gesture("Paper")
        scissors = Gesture("Scissors")
        lizard = Gesture("Lizard")
        spock = Gesture("Spock")
        rock.loses_to = [paper, spock]
        paper.loses_to = [scissors, lizard]
        scissors.loses_to = [spock, rock]
        lizard.loses_to = [scissors, rock]
        spock.loses_to = [lizard, paper]
        self.gestures_list.extend([rock, paper, scissors, lizard, spock])


    def choose_players(self):
        print (50 * "-")
        print (" ")
        num_check = False
        while num_check == False:
            num_input = input ("1 or 2 players? ")
            if num_input == "1":
                num_check = True
                print ("One player chosen.")
                return 1
            elif num_input == "2":
                print ("Two players chosen.")
                num_check = True
                return 2
            else:
                print ("Invalid option. Try again.")
                return self.choose_players()
        
    def create_players(self, number_of_players):
        if number_of_players == 1:
            player1 = Human()
            player2 = Computer()
            self.players_list.extend([player1, player2])
        else:
            player1 = Human()
            player2 = Human()
            self.players_list.extend([player1, player2])

    def start_game(self):
        player1 = self.players_list[0]
        player2 = self.players_list[1]
        print (50 * "-")
        print (" ")
        print(f"{player1.name} Vs. {player2.name}")
        print (" ")
        player1.choose_gesture(self.gestures_list)
        player2.choose_gesture(self.gestures_list)
        return player1,player2
       

    def compare(self, player1, player2):
        if player1.gesture == player2.gesture:
            print ("Draw")
        elif player1.gesture.compare(player2.gesture) == 0:
            print(f"{player1.name}'s {player1.gesture.name} loses to {player2.name}'s {player2.gesture.name}")
            player2.wins += 1
        else:
            print(f"{player1.name}'s {player1.gesture.name} beats {player2.name}'s {player2.gesture.name}")
            player1.wins += 1

        if player1.wins == 2:
            return (player1.name)
        elif player2.wins == 2:
            return (player2.name)
        else:
            player1.choose_gesture(self.gestures_list)
            player2.choose_gesture(self.gestures_list)
            return self.compare(player1, player2)
            
    def declare_winner(self, winner):
        print (" ")
        print (50 * "!")
        print (" ")
        print(f"{winner} wins!")
        print (" ")
        print (50 * "-")
        exit()