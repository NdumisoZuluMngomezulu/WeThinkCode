import sys

def lines_of_code():
    if (len(sys.argv) > 3):
        sys.exit("Too many arguments.")
    elif (len(sys.argv) < 2):
        sys.exit("Too few arguments")
    else:
        sys.argv[1]
        if (sys.argv[1].endswith(".py")):
            with open(sys.argv[1], "r") as file:
                count = 0
                for line in file:
                    if not (line.lstrip().startswith("#") or line.strip() == ""):
                        count = count + 1
        else:
            sys.exit("Not a python file")
    
    print(count)

lines_of_code()
