from time import sleep
from random import randint
from os import system

#define optional trails
trailOptions = {
        0: "Fort ahead.",
        1: "Town ahead.",
        2: "Calm road to the left",
        3: "Calm road to the right.",
        4: "Calm road straight ahead.",
        5: "Treacherous road to the right.",
        6: "Treacherous road to the left.",
        7: "Treacherous road straight ahead.",
        8: "Winding road straight ahead.",
        9: "Road crosses a river to the left.",
        10: "Road crosses a river to the right.",
        11: "Winding road crosses a river straight ahead.",
        12: "Treacherous road crosses a river straight ahead.",
        13: "Treacherous road crosses a river to the left.",
        14: "Treacherous road crosses a river to the right."
}
trailDefinitions = {
        "Fort ahead.": "You have arrived at a Fort. Collect 2 Supplies.",
        "Town ahead.": "You have arrived at a Town. Collect 1 Supply, or Remove 1 Calamity.",
        "Calm road to the left": "As you were.",
        "Calm road to the right.": "No trouble here, partner.",
        "Calm road straight ahead.": "Remain calm. Carry on.",
        "Treacherous road to the right.": "Receive one calamity.",
        "Treacherous road to the left.": "Receive one calamity.",
        "Treacherous road straight ahead.": "Receive one calamity.",
        "Winding road straight ahead.": "Receive one calamity.",
        "Road crosses a river to the left.": "Roll and Even Number to Ford the River. Roll a 1 and die by drowning. Roll a 3 or 5 and play passes to the next player.",
        "Road crosses a river to the right.": "Roll and Even Number to Ford the River. Roll an ODD number and lose a supply.",
        "Winding road crosses a river straight ahead.": "Roll a 1 and die by drowning. Roll a 3 or 5 and play passes to the next player.",
        "Treacherous road crosses a river straight ahead.": "Roll a 1 and die by drowning. Roll a 3 or 5 and play passes to the next player.",
        "Treacherous road crosses a river to the left.": "Roll and Even Number to Ford the River. Roll an ODD number and lose a supply.",
        "Treacherous road crosses a river to the right.": "Roll and Even Number to Ford the River. Roll an ODD number and lose a supply."
}
groupTrailOptions = {
        "Fort ahead.": 0,
        "Town ahead.": 0,
        "Calm road to the left.": 0,
        "Calm road to the right.": 0,
        "Calm road straight ahead.": 0,
        "Treacherous road to the right.": 0,
        "Treacherous road to the left.": 0,
        "Treacherous road straight ahead.": 0,
        "Winding road straight ahead.": 0,
        "Road crosses a river to the left.": 0,
        "Road crosses a river to the right.": 0,
        "Winding road crosses a river straight ahead.": 0,
        "Treacherous road crosses a river straight ahead.": 0,
        "Treacherous road crosses a river to the left.": 0,
        "Treacherous road crosses a river to the right.": 0
}
#define supplyoptions
supplies = {
        0: "Half a Pizza",
        1: "Bullets for your 9.",
        2: "Vicodin.",
        3: "A keg of Beer.",
        4: "A Lady's dress.",
        5: "Spare Parts.",
        6: "Two Oxen.",
        7: "A Dream Catcher",
        8: "A Mace",
        9: "A partially eaten birthday cake.",
        10: "Soylent"
}

groupSupplies = {
        "Half a Pizza": 0,
        "Bullets for your 9.": 0,
        "Vicodin.": 0,
        "A keg of Beer.": 0,
        "A Lady's dress.": 0,
        "Spare Parts.": 0,
        "Two Oxen.": 0,
        "A Dream Catcher": 0,
        "A Mace": 0,
        "A partially eaten birthday cake.": 0,
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

#execution start
#Select the number of Players.
while True:
    try:
        numPlayers = int(raw_input("Enter number of players (1-4): "))
    except ValueError:
        print "That is not a number between 1-4. Try again."
    else :
        if 1 <= numPlayers < 5:
            break
        else:
            print "That is not a number between 1-4 Try again."

playerRange = range(1, numPlayers + 1)
#Give each player a name and store it in a dictionary.
players = {}
for i in playerRange:
    name = raw_input("Enter a name for Player %s: " % i)
    players[i] = name

for i in range(numPlayers * 5):
    groupTrailOptions[trailOptions[randint(0, 14)]] += 1
    groupSupplies[supplies[randint(0, 10)]] += 1

print "The Players are:"
for player in players:
    print "Player",player,":",players[player]
print " "
print " "
print "The group has these Trail Options:"
for key in groupTrailOptions:
    if groupTrailOptions[key] != 0:
        print key,"X",groupTrailOptions[key]

print " "
print " "
print "The Group has these supplies:"
for key in groupSupplies:
    if groupSupplies[key] != 0:
        print key,"X",groupSupplies[key]

print "This journey begins in a dense forrest."
print "Your goal is to make it to the end of the Python Trail."
