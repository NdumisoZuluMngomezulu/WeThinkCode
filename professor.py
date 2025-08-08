import random

def get_level():
    n = int(input("Please enter the level between 1 and 3. \n"))
    if ((n < 1) or (n > 3)):
        n = int(input("Please re-enter the level between 1 and 3. \n"))
    elif (n = ""):
        n = int(input("Please re-enter the level between 1 and 3. \n"))
    
    exit()

def professor():
    count = 0
    guess = 0
    n = get_level()

    if (n == 1):
        for i in range(1, 11):
            x = random.randint(1,9)
            y = random.randint(1,9)
            ans = x + y
            guess = int(input(f"What is {x} + {y}: "))

            if (guess != ans):
                print("EEE")
                for i in range(1,4):
                    print(f"What is {x} + {y}: ")
            else:
                count += 1
                print("Big dawg!")

    elif (n == 2):
        for i in range(1, 11):
            x = random.randint(10,99)
            y = random.randint(10,99)
            ans = x + y
            guess = int(input(f"What is {x} + {y}: "))

            if (guess != ans):
                print("EEE")
                for i in range(1,4):
                    print(f"What is {x} + {y}: ")
            else:
                count += 1
                print("Big dawg!")
            
    else:
        for i in range(1, 11):
            x = random.randint(100,999)
            y = random.randint(100,999)
            ans = x + y
            guess = int(input(f"What is {x} + {y}: "))

            if (guess != ans):
                print("EEE")
                for i in range(1,4):
                    print(f"What is {x} + {y}: ")
            else:
                count += 1
                print("Big dawg!")
    print(f"You scored {count} out of 10.")
    exit()

professor()

            
    
