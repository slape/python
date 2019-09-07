from __future__ import annotations
from time import sleep
from random import randint, choice
from os import system
from models import Player
from trail_config import *
from run_func import *
from dataclasses import dataclass
from typing import Any, Dict, List

def game_setup() -> list[Player]:
    """Sets up game and presents opening screens."""
    print_ascii(ascii['trail'])
    print("Welcome to the Python Trial.\n")
    sleep(3)
    system('clear')

    # Select players and add them to a dictionary.
    num_players: int = select_players()
    players: list[str] = name_players(num_players)
    player_list: list[Player] = create_players(players)
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


def select_players() -> int:
    """Allows player to select a number of players between 1 and 4."""
    while True:
        try:
            num_players: int = int(input("Enter number of players (1-4): "))
        except ValueError:
            print("That is not a number between 1-4. Try again.")
            continue
        else:
            if 0 < num_players < 5:
                return num_players
                break
            else:
                print("That is not a number between 1-4. Try again.")
                continue

def name_players(num_players: int) -> list[str]:
    """Give each player a name and store them in a list."""
    players: list[str] = []
    for i in range(1, num_players + 1):
        name: str = input(f"Enter a name for Player {i}: ")
        players.append(name)
    return players

def create_players(players: list[str]) -> list[Player]:
    """Create list of player objects."""
    player_list: list[Player] = []
    for i in enumerate(players):
        supply_options: dict[str, int] = {}
        trail_options: dict[str, int] = {}
        calamities: dict[str, str] = {}
        for j in range(5):
            choic: str = choice(list(trails))
            if choic in trail_options:
                trail_options[choic] += 1
            else:
                trail_options[choic] = 1

            choi: str = choice(supplies)
            if choi in supply_options:
                supply_options[choi] += 1
            else:
                supply_options[choi] = 1
        player_num: int = i[0] + 1
        player = Player(player_num, players[i[0]], supply_options, trail_options, calamities)
        player_list.append(player)
    return player_list
