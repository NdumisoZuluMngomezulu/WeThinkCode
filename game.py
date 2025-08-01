import random

def game():

    while True:
        try:
            level = int(input("Level: "))
            if level > 0 :
                break
        except:
            continue

    rand = random.randint(1, level)
    turn = 0

    while turn != rand:
        try:
            turn = int(input("Guess: "))
            if turn < rand:
                print("Too small!")
            if turn > rand:
                print ("Too large!")
        except:
            continue
    print("Just right!")

if __name__ == "__main__":
    game()