#camel

camel = input("Input: ")
snake = " "
for i in range(len(camel)):
    if camel[i].isupper():
        snake = camel[:i] + "_" + camel[i:]
        snake = snake.lower()
    
print(snake)
