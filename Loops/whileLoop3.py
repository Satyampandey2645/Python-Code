# -------------------------------------------------------- break --------------------------------------------------------

print("Break Statement")

while True:
    user_input = input("Enter something (type 'quit' to exit): ")
    if user_input == 'quit':
        break  # Exit the loop immediately
    print(f"You entered: {user_input}")
print("Loop finished.") 


numbers = [1, -2, 3, -4, 5, -6]
index = 0

# ------------------------------------------------------ continue -------------------------------------------------------

print("\ncontinue Statement")

while index < len(numbers):
    current_number = numbers[index]
    if current_number < 0:
        index += 1
        continue  # Skip the print statement for negative numbers
    print(f"Positive number found: {current_number}")
    index += 1
print("Loop finished.")
