from time import sleep
from random import randint
from os import system

#define optional trails
trailOptions = {
        0: "Fort ahead",
        1: "Town ahead",
        2: "Calm road to the left",
        3: "Calm road to the right",
        4: "Calm road straight ahead",
        5: "Treacherous road to the right",
        6: "Treacherous road to the left",
        7: "Treacherous road straight ahead",
        8: "Winding road straight ahead",
        9: "Road crosses a river to the left",
        10: "Road crosses a river to the right",
        11: "Winding road crosses a river straight ahead",
        12: "Treacherous road crosses a river straight ahead",
        13: "Treacherous road crosses a river to the left",
        14: "Treacherous road crosses a river to the right"
}
trailDefinitions = {
        "Fort ahead": "You have arrived at a Fort. Collect 2 Supplies.",
        "Town ahead": "You have arrived at a Town. Collect 1 Supply, or Remove 1 Calamity.",
        "Calm road to the left": "As you were.",
        "Calm road to the right": "No trouble here, partner.",
        "Calm road straight ahead": "Remain calm. Carry on.",
        "Treacherous road to the right": "Receive one calamity.",
        "Treacherous road to the left": "Receive one calamity.",
        "Treacherous road straight ahead": "Receive one calamity.",
        "Winding road straight ahead": "Receive one calamity.",
        "Road crosses a river to the left": "Roll and Even Number to Ford the River. Roll a 1 and die by drowning. Roll a 3 or 5 and play passes to the next player.",
        "Road crosses a river to the right": "Roll and Even Number to Ford the River. Roll an ODD number and lose a supply.",
        "Winding road crosses a river straight ahead": "Roll a 1 and die by drowning. Roll a 3 or 5 and play passes to the next player.",
        "Treacherous road crosses a river straight ahead": "Roll a 1 and die by drowning. Roll a 3 or 5 and play passes to the next player",
        "Treacherous road crosses a river to the left": "Roll and Even Number to Ford the River. Roll an ODD number and lose a supply",
        "Treacherous road crosses a river to the right": "Roll and Even Number to Ford the River. Roll an ODD number and lose a supply."
}
groupTrailOptions = {
        "Fort ahead": 0,
        "Town ahead": 0,
        "Calm road to the left": 0,
        "Calm road to the right": 0,
        "Calm road straight ahead": 0,
        "Treacherous road to the right": 0,
        "Treacherous road to the left": 0,
        "Treacherous road straight ahead": 0,
        "Winding road straight ahead": 0,
        "Road crosses a river to the left": 0,
        "Road crosses a river to the right": 0,
        "Winding road crosses a river straight ahead": 0,
        "Treacherous road crosses a river straight ahead": 0,
        "Treacherous road crosses a river to the left": 0,
        "Treacherous road crosses a river to the right": 0
}
#define supplyoptions
supplies = {
        0: "Half a Pizza",
        1: "Bullets for your 9",
        2: "Vicodin",
        3: "A keg of Beer",
        4: "A Lady's dress",
        5: "Spare Parts",
        6: "Two Oxen",
        7: "A Dream Catcher",
        8: "A Mace",
        9: "A partially eaten birthday cake",
        10: "Soylent"
}

groupSupplies = {
        "Half a Pizza": 0,
        "Bullets for your 9": 0,
        "Vicodin": 0,
        "A keg of Beer": 0,
        "A Lady's dress": 0,
        "Spare Parts": 0,
        "Two Oxen": 0,
        "A Dream Catcher": 0,
        "A Mace": 0,
        "A partially eaten birthday cake": 0,
        "Soylent": 0
}
#define calamities
calamities = {
        0: "Kenny",
        1: "Dino",
        2: "Eating Disorder",
        3: "Soylent",
        4: "Fractal Snake",
        5: "Treason",
        6: "Extreme Cold",
        7: "Misbehaving Oxen",
        8: "Measles",
        9: "Dysentery",
        10: "Flat Tire",
        11: "Out of Steam",
        12: "Terminator",
        13: "God",
        14: "Satan",
        15: "Peyote Trip"
}

CalamityDefinitions = {
        "Kenny": "Kenny killed you.",
        "Dino": "Dino ate all your pizza and beer. You'll need a Mace to kill him and eat him or you'll die.",
        "Eating Disorder": "You've developed an eating disorder. You'll need a partially eaten birthday cake, half a pizza and some Soylent to survive.",
        "Soylent": "Rejoice! You have found some extra Soylent.",
        "Fractal Snake": "You were bitten by a Fractal Snake. You'll need bullets for your 9 to kill it before it kills you.",
        "Treason": "You're being accused of Treason. You'll need to ward off this bad luck with a dream catcher or you'll die.",
        "Extreme Cold": "Beat the cold by drinking as much beer as you can. You'll need a keg or you'll die.",
        "Misbehaving Oxen": "You Oxen were misbehaving, so another member killed them. You'll need 2 more Oxen or everyone dies.",
        "Measles": "You have the Measles. Lose a turn unless you have some Vicodin to keep going.",
        "Dysentery": "You died of Dysentery.",
        "Flat Tire": "Your steam mobile has a flat tire. You'll need spare parts to fix it or everyone dies.",
        "Out of Steam": "Your steam mobile ran out of steam. You'll need to have 2 Oxen to pull it or everyone dies.",
        "Terminator": "Terminator showed up from the future to kill you. You need to disguise yourself with a new dress or he kills you.",
        "God": "God killed you. You're dead.",
        "Satan": "Satan has decided to give you one last chance. Sit out for 2 rounds. The group cannot use your supplies.",
        "Peyote Trip": "You ate some random Peyote that you found along the way. You'll need half a pizza to get over this or you'll die."
}

ascii = {
    "trail" : "ascii_pics/trail_pic",
    "9mm" : "ascii_pics/9mm",
    "beer" : "ascii_pics/beer",
    "cactus" : "ascii_pics/cactus",
    "cake" : "ascii_pics/cake",
    "cholera" : "ascii_pics/cholera",
    "clothes" : "ascii_pics/clothes",
    "dead_oxen" : "ascii_pics/dead_oxen",
    "death" : "ascii_pics/death",
    "dice" : "ascii_pics/dice",
    "dino" : "ascii_pics/dino",
    "disentary" : "ascii_pics/disentary",
    "disorder" : "ascii_pics/disorder",
    "donQ" : "ascii_pics/donQ",
    "dream_catcher" : "ascii_pics/dream_catcher",
    "enterprise" : "ascii_pics/enterprise",
    "extreme_cold" : "ascii_pics/extreme_cold",
    "fort" : "ascii_pics/fort",
    "fractal_snake" : "ascii_pics/fractal_snake",
    "god" : "ascii_pics/god",
    "kenny" : "ascii_pics/kenny",
    "knight" : "ascii_pics/knight",
    "mace" : "ascii_pics/mace",
    "mountains" : "ascii_pics/mountains",
    "mushroom_cloud" : "ascii_pics/mushroom_cloud",
    "oxen" : "ascii_pics/oxen",
    "pizza" : "ascii_pics/pizza",
    "rain" : "ascii_pics/rain",
    "repair" : "ascii_pics/repair",
    "snake" : "ascii_pics/snake",
    "spare_parts" : "ascii_pics/spare_parts",
    "steam_wagon" : "ascii_pics/steam_wagon",
    "terminator" : "ascii_pics/terminator",
    "tornado" : "ascii_pics/tornado",
    "treason" : "ascii_pics/treason",
    "vicodin" : "ascii_pics/vicodin",
}

# Select number of players
def select_players():
    numPlayers = 0
    while numPlayers < 1:
        try:
            numPlayers = int(eval(input("Enter number of players (1-4): ")))
            if 0 < numPlayers < 5:
                return numPlayers
                print('\n')
                break
            else :
                print("That is not a number between 1-4 Try again.")
        except ValueError:
            print("That is not a number between 1-4. Try again.")

# Give each player a name and store it in a dictionary.
def name_players(num_players):
    players = {}
    for i in range(1, num_players + 1):
        name = input(f"Enter a name for Player {i}: ")
        players[i] = name
    return players

# Assign group assets. 5 random assets per player.
def assign_assets(num_players):
    for i in range(num_players * 5):
        groupTrailOptions[trailOptions[randint(0, 14)]] += 1
        groupSupplies[supplies[randint(0, 10)]] += 1

# Print player numbers and names.
def print_players(players):
    print("The Players are:")
    for player in players:
        print(f"Player {player}: {players[player]}.")

# Print group trail options.
def print_options(groupTrailOptions):
    print("The group has these Trail Options:")
    for key in groupTrailOptions:
        if groupTrailOptions[key] != 0:
            print(f"{key}: {groupTrailOptions[key]}")

# Print group supplies.
def print_supplies(groupSupplies):
    print("The Group has these supplies:")
    for key in groupSupplies:
        if groupSupplies[key] != 0:
            print(f"{key}: {groupSupplies[key]}")

# randomly increment 1 group supply
def increment_supplies():
    groupSupplies[supplies[randint(0, 10)]] += 1
    return f"You have received supplies.", print_supplies(groupSupplies)

# decrement 1 from the group supply that was used
def decrement_supplies():
    pass

# randomly increment either group supply or trail option by 1
def increment_random_asset():
    pass

# decrement 1 from the trail option that was used
def decrement_trail_option():
    pass

# randomly increment 1 trail option
def increment_trail_option():
    pass

# print an ascii art file
def print_ascii(asciiFile):
    with open(asciiFile, "r") as f:
        for i in f:
            print(i),
            sleep(.1)

# roll the dice. Return a random number between 2 and 12.
def roll_dice(total_avail):
    total = int(total_avail / 2) + 1
    first_roll = randint(1, total)
    second_roll = randint(1, total)
    print ("Rolling...")
    print_ascii(ascii['dice'])
    sleep(2)
    print(f"The first die roll is: {first_roll}.")
    sleep(.25)
    print(f"The second die roll is: {second_roll}.")
    sleep(.75)
    roll = first_roll + second_roll
    return roll

# Wait for player input
def wait():
    input("Press Enter to Continue...")

# Players choose a trail option from their hand.
def choose_trail():
    if len(groupTrailOptions) > 0:
        print_options(groupTrailOptions)
        print('\n')
        for option in trailOptions.keys:
            if option in groupTrailOptions:
                print(option)
        option = input("Choose a trail option: ")
        print(f"You chose option {option}: {trailOption[option]}.")
        decrement_trail()
    else:
        print("The group is out of options.")
        input("Press Enter to roll the dice.")
        option = roll_dice(14)
        if option == 11:
            print(f"You rolled an {option}! Receive one Trail Option.")
            incerment_trail()
        elif option == 12:
            print(f"You rolled a {option}! Receive one Supply.")
            increment_supplies()
        else :
            print(f"You rolled a {option}: {trailOption[option]}.")
    return option

# Game setup and opening screens
def game_setup():
    print_ascii(ascii['trail'])
    print("Welcome to the Python Trial.\n")
    sleep(3)
    system('clear')

    # Select players and add them to a dictionary.
    num_players = select_players()
    players = name_players(num_players)
    print_players(players)
    print('\n')

    # Assign supplies and trail options to the team.
    assign_assets(num_players)
    print_options(groupTrailOptions)
    print('\n')
    print_supplies(groupSupplies)

    wait()
    system('clear')

    # Starting message
    print("\nThis journey begins in a dense forrest.")
    print("Your goal is to make it to the end of the Python Trail.\n")
    sleep(2)
    system('clear')

    print_ascii(ascii['death'])
    print("The Trail is harsh. Good Luck.")
    wait()

# execute and reveal consequences of choosen trial. Returns number of players left.
def execute_trail(trail):
    choose_calamity()
    execute_calamity()
    choose_supply()
    execute_supply()
    pass

# A random calamity is choosen
def choose_calamity():
    pass

# execute and reveal consequences of choosen calamity. Returns dict of current calamities.
def execute_calamity(calamity):
    pass

# players choose a supply
def choose_supply():
    pass

# execute and reveal consequences of supply use
def execute_supply():
    pass


# Start Game Play
def main():

    game_setup()

    trails_traversed = 0
    while trails_traversed < 20:
        choose_trail()
        players_left = execute_trail()

        if len(players_left) == 0:
            break

        trails_traversed += 1

    if trails_traversed == 20 and len(players) > 0:
        print_ascii(ascii['trail'])
        print(f"Congratulations! You made it through the trail with {len(players_left)} left.")
        sleep(3)
        system('clear')
    else :
        print_ascii(ascii['death'])
        print(f"The Trail is harsh. Everyone died. Game over.")
        sleep(3)
        system('clear')

if __name__ == '__main__':
    main()