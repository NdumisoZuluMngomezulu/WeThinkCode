from datetime import date
import sys
from num2words import num2words

def main():
    if (len(sys.argv) > 2):
        print("Too many arguments")
    elif (len(sys.argv) < 1):
        print("Too few arguments")
    else:
        print(set_minutes())

def set_minutes():
    y_now, m_now, d_now = current_date()
    y, m, d = get_age()
    years = y_now - y
    months = m_now - m
    days = d_now - d
    minutes = 0
    minutes += years * 525600
    minutes += months * 43800
    minutes += days * 1440
    
    time = num2words(minutes)

    return time

def get_age():
    DOB = input("Date of birth in the form YYYY-MM-DD: ")
    list_DOB = DOB.split("-")
    year = int(list_DOB[0])
    month = int(list_DOB[1])
    day =  int(list_DOB[2])

    return year, month, day

def current_date():
    current_date = date.today()
    the_date = str(current_date)
    list_current = the_date.split("-")
    year_current = int(list_current[0])
    month_current = int(list_current[1])
    day_current =  int(list_current[2])

    return year_current, month_current, day_current

if __name__ == "__main__":
    main()
