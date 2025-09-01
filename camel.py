#camel

def main():
    print(camel_case())

def camel_case():
    camel = input("Input: ")
    snake = ""
    for char in camel:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char

    return snake

if __name__ == "__main__":
    main()
