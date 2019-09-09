from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, List
from run_func import *
from random import choice

@dataclass
class Trail:
    name: str
    desc: str
    player: str
    reward: str
    dice: str
    punish: bool

    @property
    def traverse_trail(self) -> str:
        """Calculates consequence of a trail (itself)"""
        if self.dice == 'even':
            roll: int = roll_dice(6)
            system('clear')
            if roll == 1:
                print_ascii(ascii['grim'])
                print(f'{self.player} has died by drowning.')
                wait()
                return 'died'

            elif roll == 3 or roll == 5:
                print_ascii(ascii['snake'])
                print(f'{self.player} has lost the rest of their turn.')
                wait()
                return 'next'

            elif roll % 2 == 0:
                print_ascii(ascii['mountains'])
                print(f'{self.player} has forded the river!')
                wait()
                return 'continue'

        elif self.dice == 'odd':
            roll = roll_dice(6)
            system('clear')
            if roll % 2 != 0:
                print_ascii(ascii['snake'])
                print(f'{self.player} has lost a supply crossing the river.')
                wait()
                return 'remove_supply'

            else:
                print_ascii(ascii['mountains'])
                print(f'{self.player} has forded the river.')
                wait()
                return 'continue'

        elif self.reward == 'supplies':
            print_ascii(ascii['fort'])
            print('You found a castle! Take it easy for a moment and look around.')
            wait()
            return 'supply'

        elif self.punish:
            return 'calamity'

        elif self.reward == 'pass':
            print_ascii(ascii['mountains'])
            print('Nothing to see here, Partner.')
            wait()
            return 'continue'

    def __repr__(self):
        """Prints out the trail info."""
        return f'{self.name}\n'
