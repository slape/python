from time import sleep
from random import randint, choice
from os import system
from models import Player
from trail_config import *
from setup_func import *
from run_func import *

# Start Game Play
def main():

    player_list = game_setup()
    trails_traversed = 0
    while len(player_list) > 0:
        for player in player_list:
            player.choose_trail()
            present_calamity()
            player.choose_supply()
            calamity_check()
            trails_traversed += 1
        if trails_traversed == 20:
            break

    if trails_traversed == 20 and len(player_list) > 0:
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
