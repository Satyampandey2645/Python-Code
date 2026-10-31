user_input = input("Enter number between 5 and 9 (or type 'quit' to exit):")
if user_input.lower() == "quit":
    print(f"You typed {user_input}. So you are quit ")
else:
    try:
        num = int(user_input)
        if num > 9 or num < 5:
            raise ValueError("Value should be between 5 and 9")
        else:
            print(f"You entered {num}")
    except Exception as e:
        print("Error:",e)