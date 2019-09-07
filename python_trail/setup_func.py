from __future__ import annotations
from time import sleep
from random import randint, choice
from os import system
from models import Player
from trail_config import *
from run_func import *
from dataclasses import dataclass
from typing import Any, Dict, List

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
    for i in enumerate(players):
        supply_options = {}
        trail_options = {}
        for j in range(5):
            choic = choice(list(trails))
            if choic in trail_options:
                trail_options[choic] += 1
            else :
                trail_options[choic] = 1

            choi = choice(supplies)
            if choi in supply_options:
                supply_options[choi] += 1
            else :
                supply_options[choi] = 1
        player_num = i[0] + 1
        player = Player(player_num, players[i[0]], supply_options, trail_options)
        player_list.append(player)
    return player_list
