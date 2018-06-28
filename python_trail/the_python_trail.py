#This is a game based on a game I remember from my childhoodself.
from time import sleep
from random import randint
from os import system
#ascii Pics

class Player(object):

    assets = {
    "pizza": 0,
    "bullets": 0,
    "vicodin": 0,
    "kegs": 0,
    "dresses": 0,
    "parts": 0,
    "oxen": 0,
    "dream_catchers": 0,
    "maces": 0,
    "cakes": 0,
    "soylent": 0,
    "road_left": 0,
    "road_right": 0,
    "road_straight": 0,
    "get_out_jail": 0,
    "phone_friend": 0 }

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        for i in assets:
            if assets[i] != 0:
                print "$s has $d $s" (name, assets[i], i)

    def increment_asset():
        pass

    def decrement_asset():
        pass

    def increment_random_asset():
        pass

playerNum = raw_input("Enter up to 4 players: ")
playerNames = []
while playerNum > 0:
    for i in playerNum:
        playerNames[i] = Player(raw_input("enter name for player %s: " % i))
        playerNum -= 1
