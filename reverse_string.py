#program to reverse words (strings)

from time import sleep

def reverse(string):
  x = len(string) -1
  newString = " "
  while x >= 0:
      newString = newString + string[x]
      x -= 1
  return newString

print "This program reverses words."
sleep(1)

word = raw_input("Enter a word to reverse. (enter 'quit' to exit): ")
print "..."
sleep(1)
while word != "quit":
    print "You entered,", word
    sleep(1)
    print word,"reversed is:",reverse(word)
    sleep(1)
    word = raw_input("Enter a word to reverse. (enter 'quit' to exit): ")
    sleep(1)

print "Quitting"
sleep(1)
print "..."
sleep(1)
print "Goodbye"
sleep(1)
