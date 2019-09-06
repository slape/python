from time import sleep
from random import randint
from os import system
from models import Player
from trail_config import *
from run_func import *

# Game setup and opening screens
def game_setup():
    print_ascii(ascii['trail'])
    print("Welcome to the Python Trial.\n")
    sleep(3)
    system('clear')

    # Select players and add them to a dictionary.
    num_players = select_players()
    players = name_players(num_players)
    player_list = create_players(players)
    print_players(player_list)
    print('\n')

    system('clear')

    # Starting message
    print("\nThis journey begins in a dense forrest.")
    print("Your goal is to make it to the end of the Python Trail.\n")
    sleep(2)
    system('clear')

    print_ascii(ascii['death'])
    print("The Trail is harsh. Good Luck.")
    wait()
    return player_list

# Select number of players
def select_players():
    numPlayers = 0
    while numPlayers < 1:
        try:
            numPlayers = int(eval(input("Enter number of players (1-4): ")))
            if 0 < numPlayers < 5:
                return numPlayers
                print('\n')
                break
            else :
                print("That is not a number between 1-4 Try again.")
        except ValueError:
            print("That is not a number between 1-4. Try again.")

# Give each player a name and store it in a dictionary.
def name_players(num_players):
    players = []
    for i in range(1, num_players + 1):
        name = input(f"Enter a name for Player {i}: ")
        players.append(name)
    return players

def create_players(players):
    player_list = []
    for i in range(len(players)):
        supps = {}
        trails = {}
        for j in range(5):
            key = randint(0, 14)
            if trailOptions[key] in trails:
                trails[trailOptions[key]] += 1
            else :
                trails[trailOptions[key]] = 1

            kei = randint(0, 10)
            if supplies[kei] in supps:
                supps[supplies[kei]] += 1
            else :
                supps[supplies[kei]] = 1

        player = Player(i + 1, players[i], supps, trails)
        player_list.append(player)
    return player_list
