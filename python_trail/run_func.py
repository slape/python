from __future__ import annotations
from time import sleep
from random import randint, choice
from os import system
from models import Player
from trail_config import *
from setup_func import *
from dataclasses import dataclass
from typing import Any, Dict, List

def print_players(players: list[Player]) -> None:
    """Print player numbers and names."""
    print("The Players are:")
    for player in players:
        print(player)
        wait()
        system('clear')

def print_ascii(asciiFile) -> None:
    """prints ascii art from text file."""
    with open(asciiFile, "r") as f:
        for i in f:
            print(i),
            sleep(.1)

def roll_dice(total_avail: int) -> int:
    """Simulates dice roll. Returns random value."""
    total: int = int(total_avail / 2) + 1
    first_roll: int = randint(1, total)
    second_roll: int = randint(1, total)
    print ("Rolling...")
    print_ascii(ascii['dice'])
    sleep(2)
    print(f"The first die roll is: {first_roll}.")
    sleep(.25)
    print(f"The second die roll is: {second_roll}.")
    sleep(.75)
    roll: int = first_roll + second_roll
    return roll

def wait() -> None:
    """Waits for player to hit enter."""
    input("Press Enter to Continue...")

def present_calamity():
    """Presents Calamity based on trail chosen."""
    pass

def calamity_check():
    """Checks for current calamities and kills a player if needed."""
    pass
