#grocery.py
def checkOUT():
    checkoutLIST = []
    count = 0;
    dictionary = {}

    try:
        while True:
            item = input("Enter item: \n")
            ITEM = item.upper()
            checkoutLIST.append(item)
    except ValueError:
        print("Error: Please enter the string.")
    except EOFError:
        pass
    
    uniqueList = list(set(checkoutLIST))

    for i in range(len(uniqueList)):
        count = checkoutLIST.count(uniqueList[i])
        dictionary.update({uniqueList[i]:count})
        print(dictionary)
        dictionary.clear()

    return '0'

print(checkOUT())
