def main():
    print(grocery())

def grocery():
    grocery_list = {}
    while True:
        try:
            item = input("Item: ").upper()
            grocery_list[item] = grocery_list.get(item, 0) + 1
        except ValueError:
            print("Please use a string")
        except EOFError:
            break

    sorted_list = sorted(grocery_list.keys())

    for item in sorted_list:
        print(f"{grocery_list[item]} {item}")
    
    
if __name__ == "__main__":
    main()

