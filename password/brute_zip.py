import sys
from zipfile import ZipFile
from time import sleep

def list_dir(zip):
  try:
    with ZipFile(zip) as zf:
      zf.printdir()
      print("\n WARNING: Never extract archives from untrusted sources without prior inspection.\n")
  except:
    print(f"""{zip} does not appear to be a .zip file.
Try running this program with a file ending in .zip""")
    print("\nExiting zipKraken.\n")
    sleep(1)
    exit()

def ask_brute():
    while True:
        yN = input("Attempt to brute force attack this .zip file with your password list (y/n)? ")
        if yN != 'y' and yN != 'n':
          print("\nNot a valid input. Enter 'y' or 'n'.")
        elif yN == 'n':
          print("\nExiting zipKraken.\n")
          sleep(1)
          exit()
        else:
          break

def brute_zip(zip, pw_file):
    #open passwords file
  with open(pw_file) as file:
    #put passwords into a list
    passwords = file.read().splitlines()
    for password in passwords:
     #encode the passwords with utf-8
      password = password.encode('utf-8')
    #open the zipfile
      with ZipFile(zip) as zf:
    #try the extract all function with each password.
          try:
            zf.extractall(pwd=password)
            print("\nSucessful with password: {password}")
            print("\nExiting zipKraken.\n")
            sleep(1)
            return True
          except:
            print(f"Tried: {password}")


def main():
  zip_file = sys.argv[1]
  passwords_file = sys.argv[2]
  print(f"\nWelcome to brute_zip. These are the files contained in {zip_file}:\n")
  sleep(1)

  list_dir(zip_file)
  ask_brute()
  if brute_zip(zip_file, passwords_file) == None:
    print("\nNone of those passwords worked.")
    print("\nExiting zipKraken.\n")
    sleep(1)

if __name__ == '__main__':
  main()
