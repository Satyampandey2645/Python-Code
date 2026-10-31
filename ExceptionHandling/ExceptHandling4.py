# Some people think there is no need for a finally block because we can write statements outside the try...except block.
# However, this does not work inside functions when return statements are used.
# This is why the finally block is important.

# Case 1: Code Outside try…except (Normal Execution)

try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occurred")    

print("I'm always executed")  


''' 
Explanation:
    * Whether exception occurs or not
    * The program does not exit early
    * The last print() executes normally

📌 Works fine outside a function
'''  