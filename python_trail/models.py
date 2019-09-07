from dataclasses import dataclass

@dataclass
class Player:
    number: int
    name: str
    supplies: dict
    trail_options: dict

    @property
    # randomly increment 1 supply
    def increment_supplies(self):
        choic = choice(supplies)
        if choic in self.supplies:
            self.supplies[choic] += 1
        else :
            self.supplies[choic] += 1
        return f'You have received {choic}.'

    # randomly increment 1 trail option
    def increment_trail_option(self):
        choic = choice(list(trails))
        if choic in self.trail_options:
            trail_options[choic] += 1
        else :
            trail_options[choic] = 1
        return f'You have received {choic}.'

    # player choose a supply
    def choose_supply(self):
        pass

    # remove a supply that was used
    def decrement_supplies(self):
        pass

    # player choose a trai
    def choose_trail(self):
        pass

    # def choose_trail():
    #     if len(groupTrailOptions) > 0:
    #         print_options(groupTrailOptions)
    #         print('\n')
    #         for option in trailOptions.keys:
    #             if option in groupTrailOptions:
    #                 print(option)
    #         option = input("Choose a trail option: ")
    #         print(f"You chose option {option}: {trailOption[option]}.")
    #         decrement_trail()
    #     else:
    #         print("The group is out of options.")
    #         input("Press Enter to roll the dice.")
    #         option = roll_dice(14)
    #         if option == 11:
    #             print(f"You rolled an {option}! Receive one Trail Option.")
    #             incerment_trail()
    #         elif option == 12:
    #             print(f"You rolled a {option}! Receive one Supply.")
    #             increment_supplies()
    #         else :
    #             print(f"You rolled a {option}: {trailOption[option]}.")
    #     return option

    # remove a trail option that was used
    def decrement_trail_option(self):
        pass

    # print player assets
    def __repr__(self):
        out = ''

        out += f'Player {self.number}: {self.name}\n'
        out += f'\nTrail Options:\n'
        for item in self.trail_options:
            out += f' {item}: {self.trail_options[item]}\n'
        out += f'\nSupplies:\n'
        for item in self.supplies:
            out += f' {item}: {self.supplies[item]}\n'

        return out
