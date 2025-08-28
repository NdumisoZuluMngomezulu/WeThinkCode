import sys
import re

def main():
    if (len(sys.argv) > 2):
        print("Too many arguments")
    elif (len(sys.argv) < 1):
        print("Too few arguments")
    else:
        parse()

def parse():
    url = input("URL: ").strip()
    username = url[-11:]
    link = "https://youtu.be/"
    link += username

    print(f"The link is: {link}")

if __name__ == "__main__":
    main()
