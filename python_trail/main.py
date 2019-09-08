from __future__ import annotations
from time import sleep
from random import randint, choice
from os import system
from models import Player
from trail_config import *
from setup_func import *
from run_func import *
from typing import Any, Dict, List
from trails import Trail

# Start Game Play
def main():
    player_list: list[Player] = game_setup()
    trails_traversed: int = 0
    while len(player_list) > 0 and trails_traversed < 10:
        for player in player_list:
            trail = player.choose_trail()
            outcome = trail.traverse_trail
            print(outcome)
            wait()
            system('clear')

            trails_traversed += 1

    if trails_traversed == 10 and len(player_list) > 0:
        print_ascii(ascii['trail'])
        print(f"Congratulations! You made it through the trail with {len(player_list)} players left.")
        sleep(2)
        system('clear')
    else :
        print_ascii(ascii['death'])
        print(f"The Trail is harsh. Everyone died. Game over.")
        sleep(2)
        system('clear')

if __name__ == '__main__':
    main()
