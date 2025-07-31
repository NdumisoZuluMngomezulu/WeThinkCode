#outdated.py
def dated(): 
    str_date = input("Enter the date in the from 'September 8 1636': \n")
    list_date = str_date.split(" ")

    try:
        month = list_date[0]
        day = list_date[1]
        year = list_date[2]
    except IndexError:
        print("Error: Please the correct date formart.")
        exit()
    
    match month:
        case "January":
            MM = "01"
        case "February":
            MM = "02"
        case "March":
            MM = "03"
        case "April":
            MM = "04"
        case "May":
            MM = "05"
        case "June":
            MM = "06"
        case "July":
            MM = "07"
        case "August":
            MM = "08"
        case "September":
            MM = "09"
        case "October":
            MM = "10"
        case "November":
            MM = "11"
        case "December":
            MM = "12"

    dateList = []
    dateList.append(year)
    dateList.append(MM)
    dateList.append(day)
    dateFormatted = "-".join(dateList)
    print(dateFormatted)

    return 0

print(dated())
