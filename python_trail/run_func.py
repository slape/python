from time import sleep
from random import randint
from os import system
from models import Player
from trail_config import *
from setup_func import *

# Print player numbers and names.
def print_players(player_list):
    print("The Players are:")
    for player in player_list:
        print(player)
        wait()
        system('clear')

# print an ascii art file
def print_ascii(asciiFile):
    with open(asciiFile, "r") as f:
        for i in f:
            print(i),
            sleep(.1)

# roll the dice. Return a random number between 2 and 12.
def roll_dice(total_avail):
    total = int(total_avail / 2) + 1
    first_roll = randint(1, total)
    second_roll = randint(1, total)
    print ("Rolling...")
    print_ascii(ascii['dice'])
    sleep(2)
    print(f"The first die roll is: {first_roll}.")
    sleep(.25)
    print(f"The second die roll is: {second_roll}.")
    sleep(.75)
    roll = first_roll + second_roll
    return roll

# Wait for player input
def wait():
    input("Press Enter to Continue...")

# A random calamity is choosen
def present_calamity():
    pass

# execute and reveal consequences of choosen calamity. Returns dict of current calamities.
def calamity_check():
    pass
