import re
import sys

def main():
    if (len(sys.argv) > 2):
        print("Too many arguments")
    elif (len(sys.argv) < 1):
        print("Too few arguments")
    else:
        print(count(input("Text: ")))


def count(string):
    matches = re.findall(r"\bum\b", string, re.IGNORECASE)
    
    return len(matches)


if __name__ == "__main__":
    main()
