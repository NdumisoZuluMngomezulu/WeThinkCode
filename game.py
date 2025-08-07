import random

def game():
    max = int(input("Please enter the max of the range. \n"))
    if (max == ""):
        print("Please enter a value. \n")
    
    ans = random.randint(1, max)
    turn = int(input(f"Enter your guess between 1 and {max} \n"))

    while (ans != turn):
        if (turn > ans):
            print("Too Large!")
        elif (turn < ans):
            print("Too small!")
        else:
            print("Just right!")
        turn = int(input(f"Enter your guess between 1 and {max} \n"))
    print("Just right!")
    
    exit()
