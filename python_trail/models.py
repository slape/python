from dataclasses import dataclass

@dataclass
class Player:
    number: int
    name: str
    supplies: dict
    trail_options: dict

    @property
    # randomly increment 1 supply
    def increment_supplies():
        groupSupplies[supplies[randint(0, 10)]] += 1
        return f"You have received supplies.", print_supplies(groupSupplies)

    # remove a supply that was used
    def decrement_supplies():
        pass

    # remove a trail option that was used
    def decrement_trail_option():
        pass

    # randomly increment 1 trail option
    def increment_trail_option():
        pass

    # player choose a supply
    def choose_supply():
        pass

    # player choose a trai
    def choose_trail():
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
