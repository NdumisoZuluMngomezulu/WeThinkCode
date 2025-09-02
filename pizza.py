import sys
import csv
from tabulate import tabulate

def main():
    if (len(sys.argv) > 2):
        sys.exit("Too many arguments")
    elif (len(sys.argv) < 2):
        sys.exit("Too few arguments")
    else:
        if (sys.argv[1].endswith(".csv")):
            headings = []
            content = []
            
            with open(sys.argv[1]) as file:
                rows = csv.DictReader(file)
                headings = rows.fieldnames
                for row in rows:
                    value = list(row.values())
                    content.append(value)

            print(tabulate(content, headings, tablefmt="grid"))

        else:
            sys.exit("Wrong file format.")
            
if __name__ == "__main__":
    main()
