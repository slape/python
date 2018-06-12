#Simple Roll the dice gambling game
from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number between 2 and 12: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum value is %d" % max_val
  guess = get_user_guess()
  if guess > max_val :
    print ("Your guess is invalid")
  else :
    print ("Rolling...")
    print"                  _______."
    print"       ______    | .   . |\ "
    print"      /     /\   |   .   |.\ "
    print"     /  '  /  \  | .   . |.'|"
    print"    /_____/. . \ |_______|.'|"
    print"    \ . . \    /  \ ' .   \ |"
    print"     \ . . \  /    \____'__\|"
    print"      \_____\/"
    sleep(2)
    print "The first die roll is %d" % first_roll
    sleep(.25)
    print "The second die roll is %d" % second_roll
    sleep(.75)
    print "My total is ", second_roll + first_roll
    sleep(2)
    total_roll = first_roll + second_roll
    print "Result..."
    sleep(2)
    if guess >= total_roll:
      print "You Win!"
    else :
      print "You Lose, Sucka!"


roll_dice(6)
