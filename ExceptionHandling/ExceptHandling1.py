a = input("Enter the number: ")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:  # this will show what the error is
    print(e)        
    
print("Some important lines of code")    
print("End of program")    

# -----------------------------------------------------------------------------------------------------------------------

a = input("Enter the number: ")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:  # this will do whatever we want when error comes
    print("Invalid input")        
    
print("Some important lines of code")    
print("End of program")    