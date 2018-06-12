from random import randint
from time import sleep
from os import system

board = []

for x in range(5):
  board.append(["O"] * 5)

def printBoard(board):
  for row in board:
    print " ".join(row)

def randomRow(board):
  return randint(0, len(board) - 1)

def randomColumn(board):
  return randint(0, len(board[0]) - 1)

shipRow = randomRow(board)
shipColumn = randomColumn(board)

print ""
sleep(.2)
print"               ___   _ _____ _____ _    ___   ___ _  _ ___ ___ "
sleep(.2)
print"              | _ ) /_\_   _|_   _| |  | __| / __| || |_ _| _ \ "
sleep(.2)
print"              | _ \/ _ \| |   | | | |__| _|  \__ \ __ || ||  _/"
sleep(.2)
print"              |___/_/ \_\_|   |_| |____|___| |___/_||_|___|_| "
print" "


print"                                     |__"
sleep(.2)
print"                                     |\/"
sleep(.2)
print"                                     ---"
sleep(.2)
print"                                     / | ["
sleep(.2)
print"                              !      | |||"
sleep(.2)
print"                            _/|     _/|-++'"
sleep(.2)
print"                        +  +--|    |--|--|_ |-"
sleep(.2)
print"                     { /|__|  |/\__|  |--- |||__/"
sleep(.2)
print"                    +---------------___[}-_===_.'____               /\ "
sleep(.2)
print"                ____`-' ||___-{]_| _[}-  |     |_[___\==--          \/   _"
sleep(.2)
print" __..._____--==/___]_|__|_____________________________[___\==--___,-----' .7"
sleep(.2)
print"|                                                                        /"
sleep(.2)
print" \_______________________________________________________________________|"

sleep(4)
system('clear')

sleep(1)
print "This is the board."
print ""
printBoard(board)
print ""
sleep(1)
print "The ship is located on one of these 'O's"
sleep(1)
print "You get 10 turns to guess the location of the ship."
print ""
sleep(1)

ready = " "
while ready != "y" and ready != "n":
    ready = raw_input("Ready? (y or n): ")
    if ready == "n":
        sleep(1)
        system('clear')
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print"                          ___                   ___               "
        sleep(.2)
        print"                         / __|__ _ _ __  ___   / _ \__ _____ _ _  "
        sleep(.2)
        print"                        | (_ / _` | '  \/ -_) | (_) \ V / -_) '_| "
        sleep(.2)
        print"                         \___\__,_|_|_|_\___|  \___/ \_/\___|_|(_)"
        sleep(2)
        system('clear')
        exit()
print "Here we go!"
print ""
sleep(1)
system('clear')
for turn in range(10):
    print ""
    printBoard(board)
    print " "
    print "Turn", turn + 1
    sleep(1)
    guessRow = int(raw_input("Guess Row (1-5): ")) - 1
    sleep(.2)
    guessColumn = int(raw_input("Guess Col (1-5): ")) - 1
    sleep(1)

    if guessRow == shipRow and guessColumn == shipColumn:
      system('clear')
      print " "
      sleep(.2)
      print"                   ___                       _        _      _   _             _        "
      sleep(.2)
      print"                 / __|___ _ _  __ _ _ _ __ _| |_ _  _| |__ _| |_(_)___ _ _  __| |       "
      sleep(.2)
      print"                | (__/ _ \ ' \/ _` | '_/ _` |  _| || | / _` |  _| / _ \ ' \(_-<_|       "
      sleep(.2)
      print"                 \___\___/_||_\__, |_| \__,_|\__|\_,_|_\__,_|\__|_\___/_||_/__(_)       "
      sleep(.2)
      print"    __   __             _     |___/ _     __  __        ___       _   _   _       ___ _    _      _ "
      sleep(.2)
      print"    \ \ / /__ _  _  / __| __ _ _ _ | |__ |  \/  |_  _  | _ ) __ _| |_| |_| |___  / __| |_ (_)_ __| |"
      sleep(.2)
      print"     \ V / _ \ || | \__ \/ _` | ' \| / / | |\/| | || | | _ \/ _` |  _|  _| / -_) \__ \ ' \| | '_ \_|"
      sleep(.2)
      print"      |_|\___/\_,_| |___/\__,_|_||_|_\_\ |_|  |_|\_, | |___/\__,_|\__|\__|_\___| |___/_||_|_| .__(_)"
      sleep(.2)
      print"                                                 |__/                                       |_|     "
      print " "

      sleep(1)
      system('clear')

      sleep(1)
      print " "
      print " "
      print " "
      print " "
      print " "
      print " "
      print"                          ___                   ___               "
      sleep(.2)
      print"                         / __|__ _ _ __  ___   / _ \__ _____ _ _  "
      sleep(.2)
      print"                        | (_ / _` | '  \/ -_) | (_) \ V / -_) '_| "
      sleep(.2)
      print"                         \___\__,_|_|_|_\___|  \___/ \_/\___|_|(_)"

      sleep(1)
      system('clear')
      break
    else :
      if guessRow not in range(5) or guessColumn not in range(5):
        print ""
        print "Oops, that's not even in the ocean."
        sleep(1)
        print ""
        system('clear')
      elif board[guessRow][guessColumn] == "X":
        print ""
        print "You guessed that one already."
        sleep(1)
        print ""
        system('clear')
      else :
        system('clear')
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        sleep(.2)
        print"                                   __  __ ___ ___ ___ _ "
        sleep(.2)
        print"                                  |  \/  |_ _/ __/ __| |"
        sleep(.2)
        print"                                  | |\/| || |\__ \__ \_|"
        sleep(.2)
        print"                                  |_|  |_|___|___/___(_)"
        print ""
        sleep(1)
        board[guessRow][guessColumn] = "X"
        system('clear')
      if turn == 9:
        system('clear')
        print ""
        print "You're out of turns."
        print " "
        sleep(1)
        printBoard(board)
        print " "
        print "The ship's location is: row:",shipRow,"Column: ",shipColumn
        sleep(3)
        system('clear')

        sleep(1)
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print"                          ___                   ___               "
        sleep(.2)
        print"                         / __|__ _ _ __  ___   / _ \__ _____ _ _  "
        sleep(.2)
        print"                        | (_ / _` | '  \/ -_) | (_) \ V / -_) '_| "
        sleep(.2)
        print"                         \___\__,_|_|_|_\___|  \___/ \_/\___|_|(_)"

        sleep(1)
        system('clear')
        sleep(1)
