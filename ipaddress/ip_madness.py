# Write code that checks to see if an IP address entered by the user is in the provided list (in the denied_connections.txt file provided for you).
#
# If it’s in the list, print “IP Address X.X.X.X found in the list at index Y” (Y = index of IP).
# Otherwise, print “IP Address X.X.X.X not found”.
# Hints:
# Don’t use a loop! Look into using the in operator.
# We haven’t talked about getting a count of occurrences in a list yet. To the Internet!
# Bonus:
# If the IP Address is in the list, have the program print an extra line:“IP Address X.X.X.X was found Z times” (Z = # times IP Address occurs in list)
# Add another initial prompt for action. It should allow for add or search actions. search behaves as above, whereas add instead adds the IP to the existing list and prints out the new list of IP addresses.
# If something other than add or search is entered (for step 2), the program should error before asking for the IP address.

from time import sleep

ips = []
with open("denied_connections.txt") as f:
    for ip in f:
        ips.append(str(ip.strip('\n')))
f.close()
print("Welcome to the IP Checker.")
print("This program checks an IP Address against a list of blocked IPs.")
print("It also allows you to add an IP Address to the list if needed.")
sleep(1)
while True:
    yN = input("Would you like to check or add an IP address? (y/n): ")
    if yN == 'y':
        choice = input("Enter 'check' or 'add': ")
        ip = input("Enter the IP address: ")

        if choice == 'check':
            if ip in ips:
                print("IP Address ", ip, " was found in the list at index: ", ips.index(ip))
                print("IP Address ", ip, " was found in the list ", ips.count(ip), " times.")
            else :
                print("IP Address " + ip + " not found")

        if choice == 'add':
            f = open("denied_connections.txt", "w+")
            f.write(ip)
            f.close()
            print("IP Address ", ip, " was added to the list.")
            print(ips)
    if yN == 'n':
        break
print("Exiting IP Program.")
sleep(1)
