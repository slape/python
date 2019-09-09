from __future__ import annotations
from time import sleep
from random import randint, choice
from os import system
from dataclasses import dataclass
from typing import Any, Dict, List
from trail_config import *

def print_players(players: list[Player]) -> None:
    """Print player numbers and names."""

    for player in players:
        print("The Players are:")
        print(player)
        wait()
        system('clear')

def print_ascii(asciiFile: str) -> None:
    """prints ascii art from text file."""
    with open(asciiFile, "r") as f:
        for i in f:
            print(i),
            sleep(.1)

def roll_dice(total_avail: int) -> int:
    """Simulates dice roll. Returns random value."""
    system('clear')
    if total_avail > 6:
        total: int = int(total_avail / 2)
        first_roll: int = randint(1, total)
        second_roll: int = randint(1, total)
        print("Rolling...")
        print_ascii(ascii['dice'])
        sleep(1)
        print(f"The first die roll is: {first_roll}.")
        sleep(.25)
        print(f"The second die roll is: {second_roll}.")
        sleep(.75)
        roll: int = first_roll + second_roll
        return roll
    else:
        roll: int = randint(1, total_avail)
        print("Rolling...")
        print_ascii(ascii['dice'])
        sleep(1)
        print(f"The die roll is: {roll}.")
        sleep(.75)
        return roll

def wait() -> None:
    """Waits for player to hit enter."""
    input("Press Enter to Continue...")
