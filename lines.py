import sys

def lines_of_code():
    if (len(sys.argv[1]) > 2):
        sys.exit("Too many arguments.")
    elif (len(sys.argv[1]) < 2):
        sys.exit("Too few arguments")
    else:
        fileName = sys.argv[1]
        if (fileName.endswith(".py")):
            with open(fileName, "r") as file:
                count = 0
                for line in file:
                    if not (line.lstrip().startswith("#") or line.strip() == ""):
                        count = count + 1
        else:
            sys.exit("Not a python file")
    
    return count


        
