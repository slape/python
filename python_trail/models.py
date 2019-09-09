from __future__ import annotations
from time import sleep
from random import randint, choice
from os import system
from trail_config import *
from typing import Any, Dict, List
from dataclasses import dataclass
from run_func import *
from trails import Trail

@dataclass
class Player:
    number: int
    name: str
    supplies: list[list]
    trail_options: list[Trail]
    calamities: list[list]

    @property
    def increment_supplies(self) -> str:
        """Randomly increment a supply option."""
        choic: str = choice(supplies)
        if choic in self.supplies:
            self.supplies[choic] += 1
        else :
            self.supplies[choic] += 1
        return f'You have received {choic}.'

    def increment_trail_option(self) -> str:
        """Randomly increment a trail option."""
        choic: str = choice(list(trails))
        if choic in self.trail_options:
            trail_options[choic] += 1
        else :
            trail_options[choic] = 1
        return f'You have received {choic}.'

    def choose_trail(self) -> Trail:
        """Player Chooses a Trail object or a random trail is chosen for them."""
        if len(self.trail_options) > 0:
            system('clear')
            print(f'\n{self.name} has these trail options.')
            for i in enumerate(self.trail_options):
                print(f'{i[0] + 1}: {i[1]} {i[1].desc}\n')

            total = len(self.trail_options)
            while True:
                try:
                    index: int = int(input(f'\nChoose an option: '))
                except ValueError:
                    print("That is not a valid choice. Try again.")
                    continue
                else:
                    if 0 < index <= total:
                        break
                    else:
                        print("That is not a valid choice. Try again.")
                        continue

            trail: Trail = self.trail_options[index - 1]
            system('clear')

            del self.trail_options[index - 1]
            return trail

        else:
            system('clear')
            print(f'Sadly, {self.name} has no trail options.')
            input(f'Press enter to roll the dice.')
            roll: int = roll_dice(14)
            trail: Trail = Trail(
                trails[roll][0],
                trails[roll][1],
                self.name,
                trails[roll][2],
                trails[roll][3],
                trails[roll][4]
                )
            system('clear')
            print(f'\nYou get option:')
            print(f'{trail}\n {trail.desc}\n')

            wait()
            system('clear')
            return trail

    def lose_supply(self, supply: list) -> None:
        del self.supplies[self.supplies.index(supply)]

    def gain_supply(self, supply: list) -> None:
        self.supplies.append(supply)

    def __repr__(self):
        """Prints out the players trail options and supplies."""
        out = ''
        out += f'\nPlayer {self.number}: {self.name}\n'

        # checks for trail options before printing.
        if len(self.trail_options) > 0:
            out += f'\nTrail Options:\n'
            for item in self.trail_options:
                out += f' {item}'
        else:
            out += f'\nSadly, {self.name} is out of trail options.\n'

        # checks for supplies before printing.
        if len(self.supplies) > 0:
            out += f'\nSupplies:\n'
            for item in self.supplies:
                out += f' {item[0]}\n'
        else:
            out += f'\nSadly, {self.name} is out of supplies.\n'

        return out
