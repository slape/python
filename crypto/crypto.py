#Script to hash passwords and credit card data from a CSV file.
import csv
import hashlib

hashed_rows = []
field_names = []
# Open the contents of UserInfo.csv using the Python CSV Library.
with open('UserInfo.csv', 'r') as csv_file:
    csv_rows = csv.DictReader(csv_file)
    for row in csv_rows:
#Add the email and cc to variables
#Utilize the SHA256 hash strategy to mask password and credit card number.
        sha256 = hashlib.sha256()
        sha256.update(row['Password'].encode())
        hashed_password = sha256.hexdigest()
        sha256.update(row['CC'].encode())
        hashed_cc = sha256.hexdigest()
#Create a new hashed row with the hashed info. Append to a list.
        hashed_row = row
        hashed_row['Password'] = hashed_password
        hashed_row['CC'] = hashed_cc
        hashed_rows.append(hashed_row)
#Store the hashed version of the data into a new file UserInfo_Hashed.csv.
with open('UserInfo_Hashed.csv', 'w') as hashed_csv:
    field_names = ['Name','Email','Password','Phone','Address','City','Zip',
    'Country','CC','CVV','Balance']
    csv_writer = csv.DictWriter(hashed_csv, fieldnames=field_names,
    delimiter=',')
    csv_writer.writeheader()
    csv_writer.writerows(hashed_rows)
