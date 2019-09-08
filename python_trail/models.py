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
    supplies: list
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
            print(f'\n{self.name} has these trail options.')
            for i in enumerate(self.trail_options):
                print(f'{i[0]}: {i[1]}')

            index: int = int(input(f'\nChoose an option: '))
            trail: Trail = self.trail_options[index]
            print(type(self.trail_options))
            print(type(trail))

            print(f'\nYou chose option: {index}')
            print(f'{trail}\n {trail.desc}\n')
            wait()

            system('clear')
            del self.trail_options[index]
            return trail

        else:
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
            print(f'\nYou get option:')
            print(trail)

            wait()
            system('clear')
            return trail

    def trail_consequence(consequence: str) -> None:
        """Calculates the consequences of a trail."""
        # print consequence
        # parse consequence
        # calculate consequence
        pass

    def choose_supply(self) -> str:
        """Player chooses a supply to use."""
        #print you have these Options

        # print choose an option

        # take in option choise

        # print you chose option -

        # return option
        pass

    def decrement_supplies(self, supply: str) -> None:
        """Player looses a supply that they choose to use."""
        # remove given supply from supplies
        pass



    def assign_calamity(self, calamity: str) -> None:
        """Assigns Calamity based on trail chosen."""
        pass

    def calamity_check(self) -> list:
        """Checks for current calamities and kills a player if needed."""
        pass

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
                out += f' {item}\n'
        else:
            out += f'\nSadly, {self.name} is out of supplies.\n'

        # checks for calamities before printing.
        if len(self.calamities) > 0:
            out += f'\nCalamities:\n'
            for item in self.calamities:
                out += f' {item}: {self.calamities[item]}\n'
        else:
            out += f'\nRejoice! {self.name} is free of calamities.\n'
        return out
