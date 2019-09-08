from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, List
from run_func import roll_dice

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
            if roll == 1:
                print(f'{self.player} has died by drowning.')
                return 'died'

            elif roll == 3 or roll == 5:
                print(f'{self.player} has lost the rest of their turn.')
                return 'next'

            elif roll % 2 == 0:
                print(f'{self.player} has forded the river.')
                return 'continue'


        elif self.dice == 'odd':
            roll = roll_dice(6)

            if roll % 2 != 0:
                print(f'{self.player} has lost a supply crossing the river.')
                return 'remove_supply'

            else:
                print(f'{self.player} has forded the river.')
                return 'continue'


        elif self.reward == 'supply':
            print(f'{self.player} has picked up a supply for the group.')
            return 'supply'

        elif self.reward == 'calamity':
            print(f'{self.player} has removed a calamity.')
            return 'resolve_calamity'

        elif self.punish:
            print(f'{self.player} has received a calamity.')
            return 'calamity'

        elif self.reward == 'pass':
            return 'continue'

        else:
            return None

    def __repr__(self):
        """Prints out the trail info."""

        return f'{self.name}\n'
