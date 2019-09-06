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
        key = randint(0, 10)
        if supplies[key] in self.supplies:
            self.supplies[supplies[key]] += 1
        else :
            self.supplies[supplies[key]] += 1
        return f'You have received {supplies[key]}.'

    # randomly increment 1 trail option
    def increment_trail_option(self):
        key = randint(0, 14)
        if trailOptions[key] in self.trail_options:
            trail_options[trailOptions[key]] += 1
        else :
            trail_options[trailOptions[key]] = 1
        return f'You have received {trailOptions[key]}.'

    # player choose a supply
    def choose_supply(self):
        pass

    # remove a supply that was used
    def decrement_supplies(self):
        pass

    # player choose a trai
    def choose_trail(self):
        pass

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
