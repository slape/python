from __future__ import annotations
from time import sleep
from random import randint, choice
from os import system
from models import Player
from trail_config import *
from setup_func import *
from run_func import *
from typing import Any, Dict, List
from trails import Trail

# Start Game Play
def main():
    player_list: list[Player] = game_setup()
    trails_traversed: int = 0
    while len(player_list) > 0 and trails_traversed < 20:
        for player in player_list:

            print(player)
            system('clear')
            trail: Trail = player.choose_trail()
            outcome: str = trail.traverse_trail

            if outcome == 'died':
                player_list.remove(player)
                trails_traversed += 1
                if trails_traversed == 20:
                    break
                continue

            elif outcome == 'next':
                continue

            elif outcome == 'remove_supply':
                supply = choice(player.supplies)
                player.lose_supply(supply)
                system('clear')
                print_ascii(ascii[supply[1]])
                print(f'{player.name} lost {supply[0]}')
                trails_traversed += 1
                if trails_traversed == 20:
                    break
                wait()
                continue

            elif outcome == 'supply':
                supply = choice(supplies)
                player.gain_supply(supply)
                system('clear')
                print_ascii(ascii[supply[1]])
                print(f'{player.name} gained {supply[0]}')
                trails_traversed += 1
                if trails_traversed == 20:
                    break
                wait()
                continue

            elif outcome == 'continue':
                trails_traversed += 1
                if trails_traversed == 20:
                    break
                continue

            elif outcome == 'calamity':
                calamity = (choice(calamities))
                system('clear')
                print_ascii(ascii[calamity[0].lower()])
                print(f'{player.name} has received a calamity.\n')
                for i in calamity:
                    print(i)
                wait()

                if calamity[0] == 'Kenny' or calamity[0] == 'God' or calamity[0] == 'Enterprise' or calamity[0] == 'Dysentery':
                    print(f'\n{player.name} died from this calamity.')
                    player_list.remove(player)
                    trails_traversed += 1
                    if trails_traversed == 20:
                        break
                    continue

                find = False
                for player in player_list:
                    for supply in player.supplies:
                        if supply[2] == calamity[0]:
                            system('clear')
                            print_ascii(ascii[supply[1]])
                            print(f'{player.name} has {supply[0]}.')
                            sleep(.75)
                            print(f'Using {supply[0]} to resolve this calamity.')
                            wait()
                            player.lose_supply(supply)
                            calamity = []
                            find = True
                            break
                    if find:
                        break
                    else :
                        system('clear')
                        print(f'{player.name} only has these supplies:')
                        for i in player.supplies:
                            print(f'{i[0]}')
                        print(f'\n{player.name} cannot resolve this calamity.')
                        wait()
                if find:
                    trails_traversed += 1
                    if trails_traversed == 20:
                        break
                    continue
                else :
                    player_list.remove(player)
                    trails_traversed += 1
                    system('clear')
                    print_ascii(ascii[calamity[0].lower()])
                    print(f'{player.name} has died from this calamity.')

                if trails_traversed == 20:
                    break
            wait()
            system('clear')

    if len(player_list) > 0:
        system('clear')
        print_ascii(ascii['end'])
        print(f"Congratulations! You made it through the trail with {len(player_list)} players left.")
        print(f'Enjoy some smores by the camp fire.')
        wait()
        system('clear')
        print_ascii(ascii['snake'])
        print('Thanks for playing the Python Trail.')
        print('Game Over.')
        sleep(3)
        system('clear')
    else :
        system('clear')
        print_ascii(ascii['death'])
        print(f"The Trail is harsh. Everyone died.")
        wait()
        system('clear')
        print_ascii(ascii['snake'])
        print('Thanks for playing the Python Trail.')
        print('Game Over.')
        sleep(3)
        system('clear')

if __name__ == '__main__':
    main()
