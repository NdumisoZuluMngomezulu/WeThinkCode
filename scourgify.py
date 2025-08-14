import csv
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if (sys.argv[1].endswith(".csv")):
            file = sys.argv[1]
            secondfile = sys.argv[2]

            try:
                with open(file) as file:
                    reader = csv.DictReader(file)
                    with open(secondfile, "w") as secondfile:
                        header = ["first", "last", "house"]
                        writer = csv.DictWriter(secondfile, fieldnames = header)
                        writer.writeheader()
                        for student in reader:
                            last, first = student["name"].split(", ")
                            house = student["house"]
                            writer.writerow({"first": first, "last": last, "house": house})
            except FileNotFoundError:
                sys.exit(f"Could not read {input}")
        else:
            sys.exit("Not a CSV File")

main()
