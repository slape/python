from random import randint
import random
from time import sleep

class Player(object):

    assets = {
    "bullets" = 0
    "vicodin" = 0
    "kegs" = 0
    "dresses" = 0
    "parts" = 0
    "oxen" = 0
    "dream_catchers" = 0
    "maces" = 0
    "cakes" = 0
    "soylent" = 0
    "road_left" = 0
    "road_right" = 0
    "road_straight" = 0
    "get_out_jail" = 0
    "phone_friend" = 0 }

    def __init__(self, name):
        self.name = name
        self.pizza = pizza

    def __repr__(self):
        for i in assets:
            if assets[i] != 0:
                print "$s has $d $s" (name, assets[i], i)

    def increment_asset():
        pass

    def decrement_asset():
        pass

    def random_asset():
        pass

asciiSupplies = {
    "pizza": "ascii_pics/pizza"
    "bullets": "ascii_pics/bullets"
    "vicodin": "ascii_pics/vicodin"
    "keg": "ascii_pics/keg"
    "dress": "ascii_pics/dress"
    "parts": "ascii_pics/parts"
    "oxen": "ascii_pics/oxen"
    "dream_catcher": "ascii_pics/dream_catcher"
    "mace": "ascii_pics/mace"
    "cake": "ascii_pics/cake"
    "soylent": "ascii_pics/soylent"}
trail = {
        "ascii_pics/fort": "You have arrived at a Fort. Collect 2 Supplies.",
        "ascii_pics/fort": "You have arrived at a Town. Collect 1 Supply, or Remove 1 Calamity.",
        "ascii_pics/donQ": "Don Quixote to the left. As you were.",
        "ascii_pics/cactus": "Catus to the right. No trouble here, partner.",
        "ascii_pics/knight": "Knight straight ahead. Rest easy. Carry on.",
        "ascii_pics/enterprise": "StarShip Enterprise blocks your path. Receive one calamity.",
        "ascii_pics/mountains": "You have to cross the Mountains. Receive one calamity.",
        "ascii_pics/mushroom_cloud": "Mushroom Cloud straight ahead. Receive one calamity.",
        "ascii_pics/rain": "It's raining. Receive one calamity.",
        "ascii_pics/rain:" "Roll and Even Number to cross the River. Roll a 1 and the man kills you.",
        "ascii_pics/tornado:": "A Tornado! Roll and Even Number to hide safely in a bunker. Roll an ODD number and lose a player.",
        "ascii_pics/dead_oxen": "You pass a deserted camp site with hanging oxen. Roll a 1 and die from bad oxen meat. Roll a 3 or 5 and play passes to the next player.",
        "ascii_pics/snake": "Rattle snake in in front of a river. Roll a 1 to kill the snake, only to die by drowing. Roll a 3 or 5 and play passes to the next player.",
        "ascii_pics/rain": "It's raning again. Roll and Even Number to push on. Roll an ODD number and lose a supply.",
        "ascii_pics/repair": "You have to stop for a wagon repair. Roll and Even Number to push on. Roll an ODD number and lose a supply."
        }
calamities = {
        "ascii_pics/kenny": "Kenny killed you.",
        "ascii_pics/dino": "Dino ate all your pizza and beer. You'll need a Mace to kill him and eat him or you'll die.",
        "ascii_pics/disorder": "You've developed an eating disorder. You'll need a partially eaten birthday cake, half a pizza and some Soylent to survive.",
        "Soylent": "Rejoice! You have found some extra Soylent.",
        "ascii_pics/fractal_snake": "You were bitten by a Fractal Snake. You'll need bullets for your 9 to kill it before it kills you.",
        "ascii_pics/treason": "You're being accused of Treason. You'll need to ward off this bad luck with a dream catcher or you'll die.",
        "ascii_pics/extreme_cold": "Beat the cold by drinking as much beer as you can. You'll need a keg or you'll die.",
        "ascii_pics/dead_oxen": "You Oxen were misbehaving, so another member killed them. You'll need 2 more Oxen or everyone dies.",
        "ascii_pics/measles": "You have the Measles. Lose a turn unless you have some Vicodin to keep you going.",
        "ascii_pics/disentary": "You died of Dysentery.",
        "ascii_pics/steam_wagon": "Your steam wagon has a flat tire. You'll need spare parts to fix it or everyone dies.",
        "ascii_pics/wagon": "Your steam mobile ran out of steam. You'll need to have 2 Oxen to pull it or everyone dies.",
        "ascii_pics/terminator": "The Terminator showed up from the future looking for you. You need to disguise yourself with a new dress or he kills you.",
        "ascii_pics/god": "God killed you. You're dead.",
        "ascii_pics/death": "Satan has decided to give you one last chance. Sit out for 2 rounds. The group cannot use your supplies.",
        "ascii_pics/cactus": "You ate some random Peyote that you found along the way. You'll need half a pizza to get over this or you'll die."}

for i in range(4 * 5):
    suppliesChoice = random.choice(supplies.items())
    supplies[suppliesChoice[0]] += 1
    trailChoice = random.choice(trailOptions.items())
    trailOptions[trailChoice[0]] += 1

print " "
print " "
print "The group has these supplies:"
for i in supplies:
    if supplies[i] > 0:
        print i, supplies[i],

print " "
print " "
print "The group has these trail options:"
for i in trailOptions:
        if trailOptions[i] > 0:
            print i, trailOptions[i],

print " "
print " "

print "Bon Voyage!"

while True:
    raw_input("Hit Enter to Start.")
    randomRoad = random.choice(trailDefinitions.items())
    print randomRoad[0], randomRoad[1]
    if randomRoad[1] == "Receive one calamity.":
        randomCalamity = random.choice(calamities.items())
        print randomCalamity[1]

ascii = {
    "cold": "ascii_pics/enterprise",
    "oxen": "ascii_pics/oxen.txt"
}

def printAscii(asciiFile):
    with open(asciiFile, "r") as f:
        for i in f:
            print i,
            sleep(.1)

printAscii(ascii["cold"])
