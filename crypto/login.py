#simple script to hash user data
import csv
import hashlib
# * Prompt users for their email address and password.
user_email = input("Enter your email address: ")
user_password = input("Enter your password: ")
# * Hash the password provided using the SHA256 strategy.
sha256 = hashlib.sha256()
sha256.update(user_password.encode())
hashed_password = sha256.hexdigest()
# * Compare the email and password provided against all records in the csv.
with open('UserInfo_Hashed.csv', 'r') as csv_file:
    csv_rows = csv.reader(csv_file)
    for row in csv_rows:
# * If a match is found, the user should be greeted with their name, address, and bank balance.
        if user_email in row and hashed_password in row:
            print(f"Hello {row[0]}.\nYour address on file is: {row[4]}\n"
            f"Your bank balance is: {row[10]}.")
            break
# * If no match is found, the user should be informed that their login attempt was invalid.
    else :
        print("Login is invalid.")
