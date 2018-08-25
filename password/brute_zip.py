import sys
from zipfile import ZipFile
from time import sleep

#List the files in the zipfile for inspection.
def list_dir(zip):
    try:
        with ZipFile(zip) as zf:
            zf.printdir()
            print("\n WARNING: Never extract archives from untrusted sources"
            "without prior inspection.\n")
    except:
        print(f"{zip} does not appear to be a .zip file.\n"
        "Try running this program with a file ending in .zip")
        print("\nExiting brute_zip.\n")
        sleep(1)
        exit()

#Ask the user if they would like to extract the zipfile.
def ask_brute():
    while True:
        yN = input("Attempt to brute force attack this .zip file with your"
        "password list (y/n)? ")
        if yN != 'y' and yN != 'n':
            print("\nNot a valid input. Enter 'y' or 'n'.")
        elif yN == 'n':
            print("\nExiting brute_zip.\n")
            sleep(1)
            exit()
        else:
            break
            
#Open the passwords file, encode each pw with utf-8 and add them to a list.
def enc_password_list(pw_file):
    passwords = []
    encoded_passwords = []
    with open(pw_file) as file:
        passwords = file.read().splitlines()
        for password in passwords:
            encoded_passwords.append(password.encode('utf-8'))
    return encoded_passwords

#Open the zipfile and try the extractall function with each password.
def brute_zip(zip, pw_file):
    passwords = enc_password_list(pw_file)
    with ZipFile(zip) as zf:
        for password in passwords:
            try:
                zf.extractall(pwd=password)
                print(f"\nSucessful with password: {password}")
                print("\nExiting brute_zip.\n")
                sleep(1)
                break
            except:
                print(f"Tried: {password}")
        else:
            print("\nNone of those passwords worked.")
            print("\nExiting brute_zip.\n")
            sleep(1)

def main():
    zip_file = sys.argv[1]
    passwords_file = sys.argv[2]
    print(f"\nWelcome to brute_zip."
    "These are the files contained in {zip_file}:\n")
    sleep(1)

    list_dir(zip_file)
    ask_brute()
    brute_zip(zip_file, passwords_file)

if __name__ == '__main__':
  main()
