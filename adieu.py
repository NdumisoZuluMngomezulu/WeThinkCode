def adieu():
    goodbye = "Adieu, adieu, to "
    list = []
    print("Enter the names and hit Ctrl + Z when you're done. \n")
    try:
        while True:
            name = input("Enter name. \n")
            list.append(name)
            if (len(list) > 1):
                comma = ","
                list.insert(-1, "and ")
                names = comma.join(list)
                sentence = goodbye + names
                print(sentence)
            else:
                sentence = goodbye + name
                print(sentence)
    except EOFError:
        pass

adieu()
