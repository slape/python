from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class Player:
    number: int
    name: str
    supplies: dict
    trail_options: dict
    calamities: dict

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

    def choose_trail(self) -> str:
        """Player Chooses a Trail or a random trail is chosen for them."""
        if len(self.trail_options) > 0:
            pass
            #print you have these Options

            # print choose an option

            # take in option choise

            # print you chose option -

            # return option

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


    def decrement_trail_option(self, trial: str) -> None:
        """Player looses a trail option that they choose to use."""
        # remove given trail option from trail options
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

        if len(self.trail_options) > 0:
            out += f'\nTrail Options:\n'
            for item in self.trail_options:
                out += f' {item}: {self.trail_options[item]}\n'
        else:
            out += f'\nSadly, {self.name} is out of trail options.\n'


        if len(self.supplies) > 0:
            out += f'\nSupplies:\n'
            for item in self.supplies:
                out += f' {item}: {self.supplies[item]}\n'
        else:
            out += f'\nSadly, {self.name} is out of supplies.\n'

        if len(self.calamities) > 0:
            out += f'\nCalamities:\n'
            for item in self.calamities:
                out += f' {item}: {self.calamities[item]}\n'
        else:
            out += f'\nRejoice! {self.name} is free of calamities.\n'
        return out
