for i in range(1, 4):
    print(i)
    break
else:
    print("Done")
    
# Output: 1 
'''
🧠 Explanation:
    -> The loop starts with i = 1 and prints 1.
    -> The break statement immediately exits the loop.
    -> The else block of a for loop executes only if the loop completes normally (i.e., without encountering a break).
    -> Since the loop is terminated by break, the else block is skipped.
    
✔️ Hence, only 1 is printed.
'''   


for i in range(1, 4):
    print(i)
else:
    print("Done")
    
# Output: 1 2 3 Done (all in next line to each other)    
'''
🧠 Explanation:
    -> The loop runs normally for i = 1, 2, 3 and prints each value.
    -> Since no break statement interrupts the loop, it completes successfully.
    -> Therefore, the else block does execute, printing "Done".

📌 Note: The trailing 4 in your message appears to be a typo and is not part of the code execution.
'''