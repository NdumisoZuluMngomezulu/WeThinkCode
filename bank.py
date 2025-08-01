def bank():
    greetings = input("Greetingsings! \n").strip().lower()
    if greetings.startswith("h"):
        if greetings.startswith("hello"):
            print("$0")
        else:
            print("$20")
    else:
        print("$100")


bank()