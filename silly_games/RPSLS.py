#Rock, Paper, Scissors, Lizzard, Spock
#Simple Game
from random import randint
from time import sleep

options = ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]
message = {"tie": "It's a tie.", "won": "You Won!", "lost": "You Lose, Sucka!"}
action = {"one": "Scissors cuts Paper", "two": "Paper covers Rock", "three": "Rock crushes Lizard", "four": "Lizard poisons Spock", "five": "Spock smashes Scissors", "six": "Scissors decapitates Lizard", "seven": "Lizard eats Paper", "eight": "Paper disproves Spock", "nine": "Spock vaporizes Rock", "ten": "Rock crushes Scissors"}
tieAction = {"ROCK": "Rock loves Lamp", "PAPER": "Papers, Papers, Papers...", "SCISSORS": "Let's cut this mother out", "LIZZARD": "Lizzards Rule", "SPOCK": "May the force be with you."}

def decideWinner(userChoice, computerChoice):
  print "You selected: %s" % userChoice
  sleep(1)
  print "I selected: %s" % computerChoice
  sleep(1)
  if userChoice == computerChoice:
    print tieAction[userChoice]
    sleep(1)
    print message["tie"]
  elif userChoice == options[2] and computerChoice == options[1]:
    print action["one"]
    sleep(1)
    print message["won"]
  elif userChoice == options[1] and computerChoice == options[2]:
    print action["one"]
    sleep(1)
    print message["lost"]
  elif userChoice == options[1] and computerChoice == options[0]:
    print action["two"]
    sleep(1)
    print message["won"]
  elif userChoice == options[0] and computerChoice == options[1]:
    print action["two"]
    sleep(1)
    print message["lost"]
  elif userChoice == options[0] and computerChoice == options[3]:
    print action["three"]
    sleep(1)
    print message["won"]
  elif userChoice == options[3] and computerChoice == options[0]:
    print action["three"]
    sleep(1)
    print message["lost"]
  elif userChoice == options[3] and computerChoice == options[4]:
    print action["four"]
    sleep(1)
    print message["won"]
  elif userChoice == options[4] and computerChoice == options[3]:
    print action["four"]
    sleep(1)
    print message["lost"]
  elif userChoice == options[4] and computerChoice == options[2]:
    print action["five"]
    sleep(1)
    print message["won"]
  elif userChoice == options[2] and computerChoice == options[4]:
    print action["five"]
    sleep(1)
    print message["lost"]
  elif userChoice == options[2] and computerChoice == options[3]:
    print action["six"]
    sleep(1)
    print message["won"]
  elif userChoice == options[3] and computerChoice == options[2]:
    print action["six"]
    sleep(1)
    print message["lost"]
  elif userChoice == options[3] and computerChoice == options[1]:
    print action["seven"]
    sleep(1)
    print message["won"]
  elif userChoice == options[1] and computerChoice == options[3]:
    print action["seven"]
    sleep(1)
    print message["lost"]
  elif userChoice == options[1] and computerChoice == options[4]:
    print action["eight"]
    sleep(1)
    print message["won"]
  elif userChoice == options[4] and computerChoice == options[1]:
    print action["eight"]
    sleep(1)
    print message["lost"]
  elif userChoice == options[4] and computerChoice == options[0]:
    print action["nine"]
    sleep(1)
    print message["won"]
  elif userChoice == options[0] and computerChoice == options[4]:
    print action["nine"]
    sleep(1)
    print message["lost"]
  elif userChoice == options[0] and computerChoice == options[2]:
    print action["ten"]
    sleep(1)
    print message["won"]
  elif userChoice == options[2] and computerChoice == options[0]:
    print action["ten"]
    sleep(1)
    print message["lost"]


def playRPSLS():
  userChoice = raw_input("Enter Rock, Paper, Scissors, Lizard or Spock: ")
  userChoice = userChoice.upper()
  computerChoice = options[randint(0, 4)]
  decideWinner(userChoice, computerChoice)

playRPSLS()
