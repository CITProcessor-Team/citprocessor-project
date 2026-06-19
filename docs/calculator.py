A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
operator = input("Enter the arithmetic operator: ")

if B == 0 and operator == "/":
    print("Error! Division by zero")
else:
    if operator == "+":
        print(A + B)
    elif operator == "-":
        print(A - B)
    elif operator == "*":
        print(A * B)
    elif operator == "/":
        print(A / B)
    else:
        print("Invalid operator")
