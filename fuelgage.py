#fuelgage
from fractions import Fraction

def fuelgage():
    inputFraction = input("Enter the fraction in the form 'x/y' ")
    listFraction = inputFraction.split('/')

    try:
        numerator = listFraction[0]
        denominator = listFraction[1]
    except ValueError:
        print("Error: Please enter an integer")
        exit()
    except IndexError:
        print("Error: Please enter using x/y")
        exit()

    if (denominator == 0):
        print("Denominator cannot be zero.")
    
    fraction = float(Fraction(numerator, denominator))
    percentage = round((fraction) * 100)

    if (percentage > 99):
        return 'F'
    elif (percentage < 1):
        return 'E'
    else:
        return percentage

print(fuelgage())
