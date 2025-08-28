expression = input("Enter the expression: \n")
number1 = int(expression[0])
operator = expression[2]
number2 = int(expression[4])
ans = 0
if (operator == "+"):
    ans = number1 + number2
    print(ans)
elif (operator == "-"):
    ans = number1 - number2
    print(ans)
elif (operator == "*"):
    ans = number1 * number2
    print(ans)
else:
    ans = number1 / number2
    print(ans)
