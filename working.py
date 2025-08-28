import re
import sys

def main():
    if (len(sys.argv) > 2):
        print("Too many arguments")
    elif (len(sys.argv) < 1):
        print("Too few arguments")
    else:
        convert()

def convert():
    str = input("Enter the time: ")
    first_list = str.split()
    number1 = first_list[0]
    number2 = first_list[3]
    to = " to "

    match number1[0]:
        case "1":
            time_1 = "1:00"
        case "2":
            time_1 = "2:00"
        case "3":
            time_1 = "3:00"
        case "4":
            time_1 = "4:00"
        case "5":
            time_1 = "5:00"
        case "6":
            time_1 = "6:00"
        case "7":
            time_1 = "7:00"
        case "8":
            time_1 = "8:00"
        case "9":
            time_1 = "9:00"
        case "10":
            time_1 = "10:00"
        case "11":
            time_1 = "11:00"
        case "12":
            time_1 = "12:00"

    match number2[0]:
        case "1":
            time_2 = "13:00"
        case "2":
            time_2 = "14:00"
        case "3":
            time_2 = "15:00"
        case "4":
            time_2 = "16:00"
        case "5":
            time_2 = "17:00"
        case "6":
            time_2 = "18:00"
        case "7":
            time_2 = "19:00"
        case "8":
            time_2 = "20:00"
        case "9":
            time_2 = "21:00"
        case "10":
            time_2 = "22:00"
        case "11":
            time_2 = "23:00"
        case "12":
            time_2 = "24:00"

    time = time_1 + to + time_2

    print(time)
            
