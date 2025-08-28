import re
import sys

def main():
    if (len(sys.argv) > 2):
        print("Too many arguments")
    elif (len(sys.argv) < 1):
        print("Too few arguments")
    else:
        validate()

def validate():
    address = input("Enter the IP Address: \n")

    if re.search(r"^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", address):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
