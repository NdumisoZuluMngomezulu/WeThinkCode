#coke.py
total = 0
while (total < 50):
    coin = int(input("Insert coins in 25, 10 and 5 cents. \n"))
    if coin in [5, 10, 25]:
        total += coin
        print(total)
        print(f"Amount due: {50 - total}")
        

print(f"Change owed: {total - 50}")
