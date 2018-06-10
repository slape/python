from random import randint
from time import sleep
# simple guessing game
# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!

print "Welcome to the guessing game."
sleep(1)
print ""
print "I'll generate a random number from 1 to 10, and you can try to guess it 3 times."
sleep(1)
print ""
print "You have 3 guesses left."

while guesses_left > 0:
  guess = int(raw_input("Enter your guess: "))
  while True:
      if guess in range(1,11):
          break
    
      print "What the hell was that??"
      sleep(2)
      guess = int(raw_input("Try guessing a number from 1-10: "))

  if guess == random_number :
    print "You win!"
    break
  guesses_left -= 1

else :
  print "You lose."
