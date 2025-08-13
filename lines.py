import sys

def lines_of_code():
    if (len(sys.argv[1]) > 2):
        print("Too many arguments.")
    elif (len(sys.argv[1]) < 2):
        print("Too few arguments")
    else:
        fileName = sys.argv[1]
        if (fileName.endswith(".py")):
            with open(fileName, "r") as file:
                count = 0
                for line in lines:
                    if not (line.)
        else:
            sys.exit("Not a python file")
    
    return count

def count_lines(file):
    try:
        counter = 0
        with open(file, "r") as f:
            for line in f:
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                    counter = counter + 1
            return counter
    except FileNotFoundError:
        sys.exit("File does not exist")

        