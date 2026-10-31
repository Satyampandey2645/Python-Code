a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if (operator == "+"):
    print("a + b =", a + b)
elif (operator == "-"):
    print("a - b =", a - b)
elif (operator == "*"):
    print("a * b =", a * b)
elif (operator == "/"):
    if (b != 0):
        print("a / b =", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")
