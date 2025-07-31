#taqueria.py
def taqueria():
    menu = {
            "baja taco": 4.25,
            "burrito": 7.50,
            "bowl": 8.50,
            "nachos": 11.00,
            "quesadilla": 8.50,
            "super burrito": 8.50,
            "super qunesadilla": 9.50,
            "taco": 3.00,
            "tortilla salad": 8.00
        }
    price = 0
    total = 0
    try:
        while True:
            key = input("Enter your order and enter Ctrl + Z when done: \n")
            price = menu.get(key)
            total += price
            print(total)
    except EOFError:
        pass
    
    return f"Total due: {total}"

print(taqueria())
'''
    print("Enter your order and enter Ctrl+D then Enter to finish:")
    try:
        while True:
    '''

