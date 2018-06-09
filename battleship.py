from random import randint
from time import sleep

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
print "Welcome to Battleship."
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
ready = raw_input("Ready? (enter y or n): ")

if ready == "n":
    print "Exiting Game"
    sleep(2)
    exit()
else :
    while ready != "y" and ready != "n":
        ready = raw_input("Please enter y or n only: ")
        if ready == "n":
            print "Exiting Game"
            sleep(2)
            exit()
    print "Here we go!"
    print ""
    sleep(1)
    for turn in range(10):
        print ""
        print "Turn", turn + 1
        sleep(1)
        guessRow = int(raw_input("Guess Row (1-5): ")) - 1
        sleep(1)
        guessColumn = int(raw_input("Guess Col (1-5): ")) - 1
        sleep(1)

        if guessRow == shipRow and guessColumn == shipColumn:
          print "Congratulations! You sank my battleship!"
          sleep(1)
          printBoard(board)
          print "Exiting Game"
          sleep(1)
          break
        else :
          if guessRow not in range(5) or guessColumn not in range(5):
            print ""
            print "Oops, that's not even in the ocean."
            sleep(1)
            print ""
            printBoard(board)
          elif board[guessRow][guessColumn] == "X":
            print ""
            print "You guessed that one already."
            sleep(1)
            print ""
            printBoard(board)
          else :
            print ""
            print "You missed my battleship!"
            print ""
            sleep(1)
            board[guessRow][guessColumn] = "X"
            printBoard(board)
          if turn == 10:
            print ""
            print "You're out of turns."
            sleep(1)
            print "The ship's location is: row:",shipRow,"Column: ",shipColumn
            print "Game Over"
            sleep(1)
            print "Exiting Game"
            sleep(1)
            print ""
