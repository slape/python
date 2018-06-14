#This is a calendar program.
#The program should behave in the following way:
#Print a welcome message to the user
#Prompt the user to view, add, update, or delete an event on the calendar
#Depending on the user's input: view, add, update, or delete an event on the calendar
#The program should never terminate unless the user decides to exit

from time import sleep, strftime

NAME = raw_input("Enter your name: ")


calendar = {}

def welcome():
  print "Welcome to your new calendar,",NAME
  print "Opening Calendar..."
  sleep(1)

welcome()
print strftime("%A, %b %d %Y")
print strftime("%H:%M:%S")
sleep(1)
print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "The calendar is empty."
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("What date? (MM/DD/YYYY): ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update successful"
      print calendar
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "The calendar is empty."
      else :
        event = raw_input("What date is the event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "The event has been deleted."
            print calendar
          else:
            print "That is not a valid event."
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(strftime("%Y")) > int(date[6:]):
        print "That is not a valid date."
        try_again = raw_input("Try again? Y for yes, N for No: ")
        try_again = try_again.upper
        if try_again == "Y":
          continue
        else :
          start = False
      else :
        calendar[date] = event
        print "The event has been added."
        print calendar



    elif user_choice == "X":
      start = False
    if user_choice != "X" and user_choice != "A" and user_choice != "V" and user_choice != "U" and user_choice != "D":
      print "That is not a valid input."
      print "Goodbye."
      break


start_calendar()
